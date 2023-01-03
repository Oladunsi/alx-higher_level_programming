#!/usr/bin/python3
number = 0
while number < 99:
    print("{:02d}".format(number), end=", ")
    number += 1
print("{}".format(number))
