from flask_restful import Api, Resource, reqparse;

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
      args = reqparse.RequestParser();
      
      args.add_argument('nome', type=str, required=True, help='The field "nome" cannot be left blank');
      args.add_argument('estrelas', type=float, required=True, help='The field "estrelas" cannot be left blank');
      args.add_argument('diaria', type=float, required=True, help='The field "diaria" cannot be left blank');
      args.add_argument('cidade', type=str, required=True, help='The field "nome" cannot be left blank');
      
      data = args.parse_args();
      
      for hotel in hoteis:
        if hotel['nome'] == data['nome']:
          return {
            'status': 'erro',
            'mensagem': 'Hotel already exists',
          }, 400;
      
      new_hotel = {
        'id': len(hoteis) + 1,
        'nome': data['nome'],
        'estrelas': data['estrelas'],
        'diaria': data['diaria'],
        'cidade': data['cidade'],
      }
      
      hoteis.append(new_hotel);
      
      return {
        'hotel': new_hotel,
        'mensagem': 'Hotel added',
        'status': 'ok',
      }, 200;
    
    def put(self, hotel_id):
      args = reqparse.RequestParser();
      
      args.add_argument('nome', type=str, required=True, help='The field "nome" cannot be left blank');
      args.add_argument('estrelas', type=float, required=True, help='The field "estrelas" cannot be left blank');
      args.add_argument('diaria', type=float, required=True, help='The field "diaria" cannot be left blank');
      args.add_argument('cidade', type=str, required=True, help='The field "nome" cannot be left blank');
      
      data = args.parse_args();
      
      for hotel in hoteis:
        if hotel_id == hotel['id']:
          hotel['nome'] = data['nome'];
          hotel['estrelas'] = data['estrelas'];
          hotel['diaria'] = data['diaria'];
          hotel['cidade'] = data['cidade'];
          
          return {
            'hotel': hotel,
            'mensagem': 'Hotel updated',
            'status': 'ok',
          }, 200;
        else :
          return {
            'status': 'erro',
            'mensagem': 'Hotel not found',
          }, 404;
        
      
      
    def delete(self, hotel_id):
      pass