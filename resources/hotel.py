from flask_restful import Api, Resource;

hoteis = [
  {
    'id': 1,
    'nome': 'Hotel A',
    'estrelas': 4.3,
    'diaria': 220,
    'cidade': 'São Paulo',
  },
  {
    'id': 2,
    'nome': 'Hotel B',
    'estrelas': 2.5,
    'diaria': 50,
    'cidade': 'Rio de Janeiro',
  },
  {
    'id': 3,
    'nome': 'Hotel C',
    'estrelas': 5,
    'diaria': 1000,
    'cidade': 'Minas Gerais',
  },
  {
    'id': 4,
    'nome': 'Hotel 5',
    'estrelas': 3.0,
    'diaria': 150,
    'cidade': 'São Paulo',
  }
];

class Hoteis(Resource):
    def get(self): 
      return {
        'hoteis': hoteis,
        'total': len(hoteis),
        'status': 'ok',
      };
      
class Hotel(Resource):
    def get(self, hotel_id): 
      for hotel in hoteis:
        if hotel['id'] == hotel_id:
          return hotel;
      
      return {
        'status': 'erro',
        'mensagem': 'Hotel not found',
      }, 404; 
    
    def post(self, hotel_id):
      pass
    
    def put(self, hotel_id):
      pass
      
    def delete(self, hotel_id):
      pass