from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
   

    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

 # aqui definimos el nombre de la  tabla person
        
class Person(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50), nullable=False)
    homeworld_uid = db.Column(db.Integer, db.ForeignKey('planet.id'))
    height= db.Column(db.Integer)
    mass= db.Column(db.Integer)
    gender= db.Column(db.String(1))
    
    #el metodo serialize convierte el objeto en un diccionario
    def serialize(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "homeworld_uid":self.homeworld_uid,
            "height":self.height,
            "mass" : self.mass,
            "gender": self.gender
            


        }
class Planet(db.Model):
    id= db.Column (db.Integer, primary_key=True)
    name= db.Column(db.String(50), nullable=False)
    diameter=db.Column (db.Integer, nullable=False)
    population=db.Column(db.Integer, nullable=False)
    climate=db.Column(db.String(50), nullable=False)
    relacionpersonaje = db.relationship("Person")
    relacionvehiculo = db.relationship("Vehicle")


    def serialize(self):
        return {
            "id" :self.id,
            "name":self.name,
            "diameter":self.diameter,
            "population":self.population,
            "climate":self.climate

        }  

class Vehicle(db.Model):
    id=   db.Column (db.Integer, primary_key=True)
    name= db.Column(db.String(50), nullable=False)
    model= db.Column(db.String(50), nullable=False)
    vehicle_class= db.Column(db.String(50), nullable=False) 
    length= db.Column(db.Integer)
    passengers= db.Column(db.Integer)
    manufacturer_id= db.Column(db.Integer, db.ForeignKey('planet.id'))
    pilot_uid= db.Column(db.Integer, db.ForeignKey('person.uid'))
    relacionpersonaje_vehiculo = db.relationship("Person")

    
    def serialize(self):
        return {
            "id" :self.id,
            "name":self.name,
            "model":self.model,
            "vehicle_class":self.vehicle_class,
            "length":self.length,
            "passenger":self.passenger,
            "manufacturer_id":self.manufacturer_id,
            "pilot_uid":self.pilot_uid

        }  
class List_favorites(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    favorito_person= db.Column(db.Integer,db.ForeignKey('person.uid'))
    favorito_planet= db.Column(db.Integer, db.ForeignKey('planet.id'))
    favorito_vehicle= db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    user_id= db.Column (db.Integer, db.ForeignKey('user.id'))
    relacionusuario_listafav = db.relationship("User")
    relacionpersonaje_listafav = db.relationship("Person")
    relacionplaneta_listafav = db.relationship("Planet")
    relacionvehiculo_listafav = db.relationship("Vehicle")


    def serialize(self):
         return {
            "id" :self.id,
            "favorito_person":self.favorito_person,
            "favorito_planet":self.favorito_person,
            "favorito_vehicle":self.favorito_vehicle,
            "user_id":self.user_id
        }

     
      
