#!/usr/bin/python3
"""
This is defines a State model that inherits form
SQLAlchemy base class and links db Tables using MySQLdb
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """Representation of state class in MySQL db

    __tablename__: a representation of state TABLE in db
                  that stores State instances
    id (sqlalchemy.Integer): instance of state.id
    name (sqlalchemy.String): instance of state.name
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
