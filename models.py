from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Set_SQL(Base):
    __tablename__ = 'sets'

    set_id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    description = Column(String(500))


class Card_SQL(Base):
    __tablename__ = 'cards'

    card_ID = Column(INTEGER(11), primary_key=True)
    set_id = Column(ForeignKey('sets.set_id'), nullable=False, index=True)
    card_order = Column(INTEGER(11))

    set = relationship('Set_SQL')


class Side_SQL(Base):
    __tablename__ = 'sides'

    side_id = Column(INTEGER(11), primary_key=True)
    set_id = Column(ForeignKey('sets.set_id'), nullable=False, index=True)
    name = Column(String(255))
    side_order = Column(INTEGER(11))

    set = relationship('Set_SQL')


class Cell_SQL(Base):
    __tablename__ = 'cells'

    cell_id = Column(INTEGER(11), primary_key=True)
    card_id = Column(ForeignKey('cards.card_ID'), nullable=False, index=True)
    side_id = Column(ForeignKey('sides.side_id'), nullable=False, index=True)
    info = Column(String(1000))

    card = relationship('Card_SQL')
    side = relationship('Side_SQL')
