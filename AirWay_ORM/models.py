from flask_sqlalchemy import SQLAlchemy  # this library provides orm things

db = SQLAlchemy()  # create object of SQLAlchemy inorder to access it

# every class create indivisual table when we call db.create_all() method

class Flight(db.Model):    
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key = True)
    origin = db.Column(db.String, nullable = False)
    destination = db.Column(db.String, nullable = False)
    duration = db.Column(db.Integer, nullable = False)

class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable = False)

class Origin(db.Model):
    __tablename__ = "origins"
    id = db.Column(db.Integer, primary_key= True)
    origin = db.Column(db.String, nullable = False)

class Destination(db.Model):
    __tablename__ = "destinations"
    id = db.Column(db.Integer, primary_key= True)
    destination = db.Column(db.String, nullable = False) 