from flask import Flask,render_template,redirect,request,url_for
from models import *


app = Flask(__name__)

# before we access database we need to set some configuration as per sqlalchemy standard
app.config[" "] = "sqlite:///airway.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()