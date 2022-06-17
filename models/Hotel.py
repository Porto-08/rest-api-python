from ast import Try
from database.sql_alchemy import database;


class HotelModel(database.Model):
  __tablename__ = 'hoteis';
  
  hotel_id = database.Column(database.Integer, primary_key=True, autoincrement=True);
  nome = database.Column(database.String(80));
  estrelas = database.Column(database.Float(precision=1));
  diaria = database.Column(database.Float(precision=2));
  cidade = database.Column(database.String(80));
  
  
  def __init__(self, nome, estrelas, diaria, cidade):
    self.nome = nome;
    self.estrelas = estrelas;
    self.diaria = diaria;
    self.cidade = cidade;
  
  def json(self, hotel_id):
    return {
      'id': hotel_id,
      'nome': self.nome,
      'estrelas': self.estrelas,
      'diaria': self.diaria,
      'cidade': self.cidade,
    };
    
  @classmethod
  def find_hotel(cls, hotel_id):
    hotel = cls.query.filter_by(hotel_id=hotel_id).first();
      
    if hotel:
      return hotel;
        
    return None;
  
  def save(self):
      database.session.add(self);
      database.session.commit();