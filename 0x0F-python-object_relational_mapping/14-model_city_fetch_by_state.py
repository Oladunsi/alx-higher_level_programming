#!/usr/bin/python3

"""lists all states in the db hbtn_0e_6_usa
   Usage: ./8-model_state_fetch_first.py <username> \
           <password> <username>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City)\
                              .filter(State.id == City.state_id)\
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
