from flask import Flask; 
from flask_restful import Api;
from resources.hotel import Hoteis, Hotel;

app = Flask(__name__);

# Configure the database path and name.  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rest-api-python.db';
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;

api = Api(app);

@app.before_first_request
def create_database():
  database.create_all();

api.add_resource(Hoteis, '/hoteis');
api.add_resource(Hotel, '/hoteis/<int:hotel_id>');

if __name__ == '__main__':
    # Iniciando banco de dados
    from database.sql_alchemy import database;
    database.init_app(app);
    app.run(debug=True);

