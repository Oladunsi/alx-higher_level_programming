#!/usr/bin/python3
for units in range(0, 10):
    for tens in range(units + 1, 10):
        if units == 8 and tens == 9:
            print("{}{}".format(units, tens))
        else:
            print("{}{}".format(units, tens), end=", ")
