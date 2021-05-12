from flask import Flask
from flask import render_template,request,url_for,redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('sqlite:///D:\\SEM-5\\Python Programming-2\\assignment2_5.db')  # create engine object by third party library(sqlalchemy) that is used to manage coonection to the database
db = scoped_session(sessionmaker(bind=engine)) # create session for multiple user to saperate them and return object to run SQl command

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/result',methods=["GET","POST"])
def result():
    if request.method == "POST":
        id_ = int(request.form.get("flight"))
        ps = str(request.form.get("passenger")).capitalize()
        flight = []
        if db.execute("SELECT origin,destination FROM flights WHERE id = :id",{"id":id_}).rowcount == 0:
            return render_template("error.html",error = "NO SUCH FLIGHT WITH THAT ID !!")
        flight = db.execute("SELECT origin,destination FROM flights WHERE id = :id",{"id":id_}).fetchone()
        r = db.execute("SELECT * FROM passengers WHERE name = :name",{"name":ps}).fetchall()
        if len(r)!=0:
            return render_template("error.html",error = "PASSENGER ALREADY EXISTS !!")
        db.execute("INSERT INTO passengers (name,flight_id) VALUES (:name,:flight_id)",{"name":ps,"flight_id":id_})
        plist = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",{"flight_id":id_}).fetchall()
        db.commit()
        #return "Add Successfully"
        return render_template("result.html",flight=flight,passengers=plist)
    else:
        return render_template("error.html",error = "POST REQUEST ALLOWED ONLY !!")

@app.route('/aflight')
def addFlight():
    return "Comming Soon"

@app.route('/apaseenger')
def addPassenger():
    std = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    return render_template("index.html",flights = std)

@app.route('/gflight')
def getFlight():
    return "Comming Soon"

@app.route('/gpassenger')
def getPassenger():
    return "Comming Soon"

if __name__ == "__main__":
    app.run(debug=True) 