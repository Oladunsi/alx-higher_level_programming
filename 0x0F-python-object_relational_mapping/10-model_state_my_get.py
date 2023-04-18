#!/usr/bin/python3

"""lists all states in the db hbtn_0e_6_usa
   Usage: ./8-model_state_fetch_first.py <username> \
           <password> <username>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    status = False,
    for state in session.query(State).order_by(State.id):
        if state.name == sys.argv[4]:
            status = (True, state.id)
            break
    if status[0]:
        print("{}".format(status[1]))
    else:
        print("Not found")
