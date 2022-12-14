from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets (db.Model):
    id =db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gravity = db.Column(db.Integer, unique=False, nullable=False)
    rotation_period = db.Column(db.Integer, unique=False, nullable=False)   
    orbital_period =  db.Column(db.Integer, unique=False, nullable=False) 
    population = db.Column(db.Integer, unique=False, nullable=False)
    def serialize(self):
        return {
            "id" :self.id,
            "name":self.name,
            "gravity":self.gravity,
            "rotation_period": self.rotation_period,
            "orbital_period" : self.orbital_period,
            "population" : self.population,
        }       

