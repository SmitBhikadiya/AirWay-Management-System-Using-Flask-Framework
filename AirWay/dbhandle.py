from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
import csv

engine = create_engine('sqlite:///D:\\SEM-5\\Python Programming-2\\assignment2_5.db')
db = scoped_session(sessionmaker(bind=engine))

'''
            CREATE TABLE IF NOT EXISTS flights(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                origin TEXT NOT NULL,
                destination TEXT NOT NULL,
                duration INTEGER NOT NULL
            );
    '''
'''
            CREATE TABLE IF NOT EXISTS Passengers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                flight_id INTEGER NOT NULL,
                FOREIGN KEY flight_id REFERENCES flights (id)
            );
    '''

def main():
    
    # Add file into database from csv file
    #f = open("Flask Project\AirWay\externalFile\\passengerslist.csv")
    #reader_ = csv.reader(f)
    
    #for name, flight_id in reader_:
        #db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name,:flight_id)",{"name":name,"flight_id":flight_id})
    
    #db.execute("DELETE FROM passengers")
    #rows = db.execute("SELECT name,origin,destination FROM flights JOIN passengers ON passengers.flight_id = flights.id").fetchall()
    #for row in rows:
    #    print(f"name : {row[0]} on flights {row[1]} to {row[2]}")
    db.commit()
    
     
if __name__ == "__main__":
    main()

