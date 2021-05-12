from os import environ
from flask import Flask,render_template,redirect,request,url_for
from models import *


app = Flask(__name__)

# before we access database we need to set some configuration as per sqlalchemy standard
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///airway.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/apaseenger')
def addPassenger():
    flights  = Flight.query.all()
    return render_template('addPassenger.html',flights=flights)

@app.route('/rAddpassenger',methods=["POST","GET"])
def rAddPassenger():
    emsg = []
    smsg = []
    pname = str(request.form.get("pname")).upper()
    if pname != "":
        flight_id = request.form.get('fids')
        flight = Flight.query.get(flight_id)
        if flight is not None:
            passenger = Passenger.query.filter_by(name=pname).first()
            if passenger is None:
                p = Passenger(name=pname,flight_id=flight_id)
                db.session.add(p)
                db.session.commit()
                smsg.append("Passenger add succesfully on flight : "+str(flight.origin)+" to "+str(flight.destination))
            else:
                emsg.append("Passenger is already exists on flight : "+str(flight.origin)+" to "+str(flight.destination))
        else:
            emsg.append("Flight is not exists!")
    else:
        emsg.append("Passenger name cant be empty!")
    return render_template('error.html',error=emsg,success=smsg,curl=url_for('addPassenger'))



@app.route('/aflight')
def addFlight():
    orig = Origin.query.all()
    dest = Destination.query.all()
    flight_detailes = Flight.query.all()
    return render_template("addFlights.html",origins=orig,destinations=dest,flights=flight_detailes)

@app.route('/rAddflight',methods=["GET","POST"])
def rAddFlight():
    emsg = []
    smsg = []
    
    # origin varify
    o_id = int(request.form.get('oids'))
    oobj = Origin.query.filter_by(id=o_id).first()
    if oobj is None:
        emsg.append("Origin id is not found")
    else:
        smsg.append("Origin id is found")
        origin = oobj.origin

    # destination varify   
    d_id = int(request.form.get('dids'))
    dobj = Destination.query.get(d_id)
    if dobj is None:
        emsg.append("Destination id is not found")
    else:
        smsg.append("Destination id is found")
        destination = dobj.destination

    # if both are not varify
    if oobj == None or dobj == None:
        return render_template('error.html',error=emsg,success=smsg,curl=url_for('addFlight'))
    #return "Hoo"
    if origin == destination:
        emsg.append("Origin and Destination can't be same")
        return render_template('error.html',error=emsg,success=smsg,curl=url_for('addFlight'))
    
    flight = Flight.query.filter_by(origin=origin,destination=destination).first()
    if flight is not None:
        emsg.append("Flight's Origin and Destination are already exists")
        return render_template('error.html',error=emsg,success=smsg,curl=url_for('addFlight'))
    
    durs = request.form.get('dura')
    flight = Flight(origin=origin,destination=destination,duration=durs)
    db.session.add(flight)
    db.session.commit()
    return redirect(url_for('addFlight')) 

@app.route('/aRoute')
def addRoute():
    return render_template('addRoute.html')

@app.route('/rAddRoute',methods=["GET","POST"])
def rAddRoute():
    o_name = str(request.form.get("orig")).capitalize()
    d_name = str(request.form.get("dest")).capitalize()

    smsg = []
    emsg = []
    if o_name != "":
        rorigin = Origin.query.filter_by(origin=o_name).first()
        if rorigin is not None:
            emsg.append("Origin Is Already Exists")
        else:
            smsg.append("Origin Add Successfully")
            orig = Origin(origin=o_name)
            db.session.add(orig)
            db.session.commit()

    if d_name != "":
        rdestination = Destination.query.filter_by(destination = d_name).first()
        if rdestination is not None:
            emsg.append("DESTINATION IS ALREADY EXISTS")
        else:
            smsg.append("Destination Add Successfully")
            dest = Destination(destination=d_name)
            db.session.add(dest)
            db.session.commit()
    if d_name == o_name == "":
        return redirect(url_for('addFlight'))
    else:
        if len(emsg) != 0 or len(smsg) != 0:
            if len(emsg) == 0: emsg.append("No Error")
            return render_template('error.html',error=emsg,success=smsg,curl=url_for('addFlight'))
    return redirect(url_for('addFlight'))

@app.route('/gflight/<id_>')
def getFlight(id_):
    id_ = int(id_)
    flight = Flight.query.get(id_)
    if flight is not None:
        passenger = Passenger.query.filter_by(flight_id = id_).all()
        return render_template('getFlights.html',flight=flight,passengers=passenger)
    else:
        return render_template('error.html',error=["Flight is not exists!!"],success=[],curl=url_for('addFlight'))

@app.route('/gpassenger')
def getPassenger():
    return "Comming Soon"

@app.route("/rmvRoute")
def removeRoute():
    return "removeRoute"

@app.route("/updRoute")
def updateRoute():
    return "updateRoute"

if __name__ == "__main__":
   app.run(debug=True) 