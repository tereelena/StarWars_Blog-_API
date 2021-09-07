"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Person, Planet, Vehicle, List_favorites
#from models import Person
# aca van las configuraciones iniciales de nuestro proyecto
app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)
#fin de configuraciones iniciales

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_all_user():
    # esta varibale estoy consultando a la base de datos por todos los registros de la tabla users
    all_users= User.query.all()
    all_users= list(map(lambda x: x.serialize(),all_users))
    return jsonify(all_users), 200
"""
    Single user
""" 
@app.route('/user/<int:user_id>', methods=['GET'])  
def get_single_user(user_id):
    # esta variable esta consultando a la BD por un usuario en especifico
    oneuser= User.query.get(user_id)
    return jsonify(oneuser.serialize()), 200    
"""
    All person
""" 
  
@app.route('/person', methods=['GET'])  
def get_all_people():
    #esta variable esta consultando a la base de datos por todois los registro de la tabla personajes    
    all_person= Person.query.all()
    all_person= list(map(lambda x: x.serialize(),all_person))
    return jsonify(all_person), 200

"""
    Single person
""" 
@app.route('/person/<int:person_id>', methods=['GET'])  
def get_single_people(person_id):
    # esta variable esta consultando a la BD por un personaje en especifico
    oneperson= Person.query.get(person_id)
    return jsonify(oneperson.serialize()), 200

"""
    All planets
    
"""     

@app.route('/planet', methods=['GET']) 
def get_all_planet():
    all_planet= Planet.query.all()
    all_planet= list(map(lambda x: x.serialize(),all_planet))
    return jsonify(all_planet), 200

"""
    Single planet
""" 
@app.route('/planet/<int:planet_id>', methods=['GET'])  
def get_single_planet(planet_id):
    # esta variable esta consultando a la BD por un planeta en especifico
    oneplanet= Planet.query.get(planet_id)
    return jsonify(oneplanet.serialize()), 200

"""
    All vehicles
"""     

@app.route('/vehicle', methods=['GET']) 
def get_all_vehicle():
    all_vehicle= Vehicle.query.all()
    all_vehicle= list(map(lambda x: x.serialize(),all_vehicle))
    return jsonify(all_vehicle), 200    

"""
    All favorite´s oneuser
""" 
@app.route('/list_favorites/<int:user_id>', methods=['GET']) 
def get_all_favorites(user_id):
    all_favorites= List_favorites.query.get(user_id)
    return jsonify(all_favorites.serialize()), 200

    

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
