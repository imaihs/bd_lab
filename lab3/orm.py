from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from base import Base



class Stadium(Base):
    __tablename__ = 'stadium'
    id_stadium = Column('id_stadium', Integer, primary_key=True, autoincrement=True)
    adress = Column('adress', String(99))
    number_of_seats = Column('number_of_seats', Integer)
    stadium_football_match = relationship('Football_match', cascade='delete')

    def __repr__(self):
        return "<Stadium(id_stadium='{}', adress='{}', number_of_seats='{}')>".format(self.id_stadium,self.adress,
                                                                                      self.number_of_seats)


class Football_match(Base):
    __tablename__ = 'football_match'
    id_football_match = Column('id_football_match', Integer, primary_key=True, autoincrement=True)
    who_is_play = Column('who_is_play', String(50))
    start_match = Column('start_match', Date)
    end_match = Column('end_match', Date)
    stadium = Column('stadium', Integer, ForeignKey('Stadium.id_stadium', onupdate='cascade'), primary_key=True)
    football_match_ticket = relationship('Ticket', cascade='delete')

    def __repr__(self):
        return "<Football_match(id_football_match='{}', who_is_play='{}', start_match='{}', end_match='{}')>".format(
                                                                                                   self.id_football_match,
                                                                                                   self.who_is_play,
                                                                                                   self.start_match,
                                                                                                   self.end_match)


class Ticket(Base):
    __tablename__ = 'ticket'
    id_ticket = Column('id_ticket', Integer, primary_key=True, autoincrement=True)
    cost = Column('cost', Integer)
    seat_in_the_train = Column('seat_in_the_train', Integer)
    material = Column('material', String(50))
    football_match = Column('football_match', Integer, ForeignKey('Football_match.id_football_match', onupdate='cascade'), primary_key=True)

    def __repr__(self):
        return "Ticket(id_ticket='{}', cost='{}', seat_in_the_train='{}', material='{}'".format(self.id_ticket,
                                                                                                self.cost,
                                                                                                self.seat_in_the_train,
                                                                                                self.material)


def get_class_by_name(tablename):
    for _class in [Ticket, Football_match, Stadium]:
        if hasattr(_class, '__tablename__') and _class.__tablename__ == tablename:
            return _class


def get_name_attr_of_class(table_name):
    return [attr.name for attr in dir(get_class_by_name(table_name)) if isinstance(attr, Column)]
