#!/usr/bin/python3

"""lists all states in the db hbtn_0e_6_usa
   Usage: ./8-model_state_fetch_first.py <username> \
           <password> <username>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City 
from relationship_state import State


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Califionia")
    new_state.cities = [City(name="San Francisco")]
    session.add(new_state)
    session.commit()
    session.close()
