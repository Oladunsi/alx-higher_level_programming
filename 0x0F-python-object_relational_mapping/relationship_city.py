#!/usr/bin/python3
"""
This is defines a State model that inherits form
SQLAlchemy base class and links db Tables using MySQLdb
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Representaion of state class in MySQL db
    __name__: a representation of state City in db that
             stores City instances
    id (sqlalchemy.Integer): instance of city.id
    name (sqlalchemy.String): instance of city.name
    state_id (sqlalchemy.Integer):instance of a city.state_id (Foreign Key)
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=True)
