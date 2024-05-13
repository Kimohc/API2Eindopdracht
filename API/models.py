from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class Dier(Base):
    __tablename__ = 'dieren'

    dier_id = Column(Integer, primary_key=True, index=True)
    naam = Column(String(50), unique=True)
    soort = Column(Integer)
    foto = Column(String(1000))
    geslacht = Column(String(100))
    ras = Column(String(100))
    commentaar = Column(String(1000))
    geboorte_datum = Column(String(100))


class Soort(Base):
    __tablename__ = 'dier_soorten'

    soort_id = Column(Integer, primary_key=True, index=True)
    naam = Column(String(255))


class users(Base):
    __tablename__ = 'gebruikers'
    gebruiker_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    password = Column(String(255))


class Reservering(Base):
    __tablename__ = 'reserveringen'
    reservering_id = Column(Integer, primary_key=True, index=True)
    dier_id = Column(Integer)
    gebruiker_id = Column(Integer)
