from random import randint
from flask_restful import Resource, reqparse;
from models.Hotel import HotelModel;

class Hoteis(Resource):  
  def get(self):
    try:
      hoteis = HotelModel.get();
      
      # Retorna um json com todos os hoteis
      hoteisJson = [hotel.json(hotel.hotel_id) for hotel in hoteis];
      
      return {
        'status': 'success',
        'hoteis': hoteisJson,
        'total': len(hoteis),
      }
    except Exception as e:
      return {
        'status': 'error',
        'message': 'Erro ao buscar hoteis',
        'error': str(e),
      }
    
class Hotel(Resource):
    args = reqparse.RequestParser();
    args.add_argument('nome', type=str, required=True, help='The field "nome" cannot be left blank');
    args.add_argument('estrelas', type=float, required=True, help='The field "estrelas" cannot be left blank');
    args.add_argument('diaria', type=float, required=True, help='The field "diaria" cannot be left blank');
    args.add_argument('cidade', type=str, required=True, help='The field "nome" cannot be left blank');
      
    def get(self, hotel_id): 
      hotel = HotelModel.find_hotel(hotel_id);
    
      
      if hotel:
        return hotel.json(hotel.hotel_id);
      
      return {
        'status': 'erro',
        'mensagem': 'Hotel not found',
      }, 404; 
    
    def post(self, hotel_id):
      if HotelModel.find_hotel(hotel_id):
        return {
            'status': 'erro',
            'mensagem': 'Hotel already exists',
        }, 400;
         
      data = self.args.parse_args();
      hotel = HotelModel(**data);
      
      try:
        hotel.save();
        
        return {
          'hotel': hotel.json(hotel.hotel_id),
          'mensagem': 'Hotel saved successfully',
          'status': 'ok',
        }, 200;
        
      except Exception as e:
        return {
          'status': 'erro',
          'mensagem': 'An error occurred inserting the hotel',
          'error': str(e),
        }, 500;
        
    def put(self, hotel_id):
      data = self.args.parse_args();      
      hotelFinded = HotelModel.find_hotel(hotel_id);
      
      if hotelFinded:
        try:
          hotelFinded.update(**data);
                      
          return {
            'hotel': hotelFinded.json(hotelFinded.hotel_id),
            'mensagem': 'Hotel updated',
            'status': 'ok',
          }, 200;
          
        except Exception as e:
          return {
            'status': 'erro',
            'mensagem': 'An error occurred updating the hotel',
          }, 500;
          
      return {
        'status': 'erro',
        'mensagem': 'Hotel not found',
      }
          
        
    def delete(self, hotel_id):
      hotel = HotelModel.find_hotel(hotel_id);

      if hotel:
          hotel.delete();
          
          return {
            'status': 'ok',
            'mensagem': 'Hotel deleted',
          }, 200;
        
      return {
        'status': 'erro',
        'mensagem': 'Hotel not found',
      }, 404;