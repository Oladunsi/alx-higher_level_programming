#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""@author: Oke Oladunsi Samuel
   dated: Sun 4 Aug 13:21:33 2023
"""

import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 5:
        print("Entry Not Correct!!!\n \
                Usage:{}  Username Password Database_name".format(args[0]))
        exit(1)

    username = args[1]
    password = args[2]
    database_name = args[3]
    state_name = args[4]
    db = MySQLdb.connect(host='localhost', user=username,
                         password=password, db=database_name, port=3306)
    cur = db.cursor()
    num_rows = cur.execute("SELECT * FROM `cities` AS c \
                           INNER JOIN `states` AS s \
                           ON `c`.`state_id` = `s`.`id` \
                           ORDER BY `c`.`id`;")
    rows = cur.fetchall()
    city = []
    for row in rows:
        if row[4] == state_name:
            city.append(row[2])
    print(", ".join(city))
