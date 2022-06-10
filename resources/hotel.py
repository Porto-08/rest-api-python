from random import randint
from flask_restful import Api, Resource, reqparse;

hoteis = [
  {
    'id': randint(1, 1000 * 4),
    'nome': 'Hotel A',
    'estrelas': 4.3,
    'diaria': 220,
    'cidade': 'São Paulo',
  },
  {
    'id': randint(1, 1000 * 4),
    'nome': 'Hotel B',
    'estrelas': 2.5,
    'diaria': 50,
    'cidade': 'Rio de Janeiro',
  },
  {
    'id': randint(1, 1000 * 4),
    'nome': 'Hotel C',
    'estrelas': 5,
    'diaria': 1000,
    'cidade': 'Minas Gerais',
  },
  {
    'id': randint(1, 1000 * 4),
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
    args = reqparse.RequestParser();
    args.add_argument('nome', type=str, required=True, help='The field "nome" cannot be left blank');
    args.add_argument('estrelas', type=float, required=True, help='The field "estrelas" cannot be left blank');
    args.add_argument('diaria', type=float, required=True, help='The field "diaria" cannot be left blank');
    args.add_argument('cidade', type=str, required=True, help='The field "nome" cannot be left blank');
      
    def find_hotel(self, hotel_id):
      for hotel in hoteis:
        if hotel['id'] == hotel_id:
          return hotel;
  
    def get(self, hotel_id): 
      hotel = self.find_hotel(hotel_id);
      
      if hotel:
        return hotel;
      
      return {
        'status': 'erro',
        'mensagem': 'Hotel not found',
      }, 404; 
    
    def post(self, hotel_id):
      data = self.args.parse_args();
      
      for hotel in hoteis:
        if hotel['nome'] == data['nome']:
          return {
            'status': 'erro',
            'mensagem': 'Hotel already exists',
          }, 400;
      
      new_hotel = {
        'id': randint(1, 1000 * len(hoteis)),
        **data,
      };
      
      hoteis.append(new_hotel);
      
      return {
        'hotel': new_hotel,
        'mensagem': 'Hotel added',
        'status': 'ok',
      }, 200;
    
    def put(self, hotel_id):
      data = self.args.parse_args();
      
      hotel = self.find_hotel(hotel_id);
      
      updated_hotel = {
        'id': hotel_id,
        **data,
      }
      
      if hotel:
        hotel.update(updated_hotel);
          
        return {
          'hotel': hotel,
          'mensagem': 'Hotel updated',
          'status': 'ok',
        }, 200;
          
      return {
        'status': 'erro',
        'mensagem': 'Hotel not found',
      }, 404;
        
      
      
    def delete(self, hotel_id):
      hotel = self.find_hotel(hotel_id);

      if hotel:
          hoteis.remove(hotel);
          
          return {
            'status': 'ok',
            'mensagem': 'Hotel deleted',
          }, 200;
        
      return {
        'status': 'erro',
        'mensagem': 'Hotel not found',
      }, 404;