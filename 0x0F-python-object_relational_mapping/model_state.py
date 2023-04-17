#!/usr/bin/python3
"""
This is defines a State model that inherits form
SQLAlchemy base class and links db Tables using MySQLdb
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Representation of state class in MySQL db

    __tablename__: an representation of state TABLE in db
                  that stores State instances
    id (sqlalchemy.Integer): instance of state.id
    name (sqlalchemy.String): instance of state.name
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
