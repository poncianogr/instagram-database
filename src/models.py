import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


Base = declarative_base()

#encima para que lo recoja primero y cree las tablas

# favorits_planets = Table('favorits_planets',Base.metadata ,  <== importante el Base.metadata para la creación y relación de las tablas
    
#     Column('user_id', Integer(), ForeignKey('user.id'), primary_key=True),
#     Column('planets_id', Integer(), ForeignKey('planets.id'), primary_key=True),
    
# )

# favorits_characters = Table('favorits_characters',Base.metadata,
    
#    Column('user_id', Integer(), ForeignKey('user.id'), primary_key=True),                                         
#    Column('characters_id', Integer(), ForeignKey('characters.id'), primary_key=True))

class User(Base):

    __tablename__="user"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    username = Column(String(40), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }

class People(Base):
    
    __tablename__="people"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    height = Column(String(80), unique=False, nullable=False)
    mass = Column(String(100), unique=False, nullable=False)
    hair_color = Column(String(100), unique=False, nullable=False)
    skin_color = Column(String(100), unique=False, nullable=False)
    eye_color = Column(String(100), unique=False, nullable=False)
    birth_year = Column(String(100), unique=False, nullable=False)
    gender = Column(String(100), unique=False, nullable=False)
    # favorits_characters = relationship('User', secondary = favorits_characters ) <= se le añade en las key de la tabla relacionada

    def __repr__(self):
        return f'<People id={self.id} name={self.name} height={self.height} mass={self.mass} hairColor={self.hair_color} skinColor={self.skin_color} eyeColor={self.eye_color} birthYear={self.birth_year} gender={self.gender}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair color": self.hair_color,
            "skin color": self.skin_color,
            "eye color": self.eye_color,
            "birth year": self.birth_year,
            "gender": self.gender
            # do not serialize the password, its a security breach
        }

class Planet(Base):

    __tablename__="planet"
    id = Column(Integer, primary_key=True)
    name= Column(String(100), unique=True, nullable=False)
    rotation_period= Column(String(100), unique=False, nullable=False)
    orbital_period= Column(String(100), unique=False, nullable=False)
    diameter= Column(String(100), unique=False, nullable=False)
    climate= Column(String(100), unique=False, nullable=False)
    gravity= Column(String(100), unique=False, nullable=False)
    terrain= Column(String(100), unique=False, nullable=False)
    surface_water= Column(String(100), unique=False, nullable=False)
    population= Column(String(100), unique=False, nullable=False)
    # favorits_planets = relationship('User', secondary = favorits_planets ) <= se le añade en las key de la tabla relacionada

    def __repr__(self):
        return f'<Planet id={self.id} name={self.name} rotationPeriod={self.rotation_period} orbitalPeriod={self.orbital_period} diameter={self.diameter} climate={self.climate} gravity={self.gravity} terrain={self.terrain} surfaceWater={self.surface_water} population={self.population}>' 

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name, 
            "rotationPeriod": self.rotation_period, 
            "orbitalPeriod": self.orbital_period, 
            "diameter": self.diameter, 
            "climate": self.climate, 
            "gravity": self.gravity, 
            "terrain": self.terrain, 
            "surfaceWater": self.surface_water, 
            "population": self.population
            # do not serialize the password, its a security breach
        }

class FavPlanet(Base):

    __tablename__="favPlanet"
    user_id=Column(Integer, ForeignKey("user.id"), primary_key=True)
    planet_id=Column(Integer, ForeignKey("planet.id"), primary_key=True)

    def __repr__(self):
        return f'<FavPlanet user={self.user_id} planet_id={self.planet_id}/>'

    def serialize(self):
        return {
            "username": self.user_id,
            "favorite planet": self.planet_id
        }

class FavPeople(Base):

    __tablename__="favPeople"
    user_id=Column(Integer, ForeignKey("user.id"), primary_key=True)
    people_id=Column(Integer, ForeignKey("people.id"), primary_key=True)

    def __repr__(self):
        return f'<FavPeople user={self.user_id} fav_people={self.people_id}/>'

    def serialize(self):
        return {
            "username": self.user_id,
            "favorite people": self.people_id
        }
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')