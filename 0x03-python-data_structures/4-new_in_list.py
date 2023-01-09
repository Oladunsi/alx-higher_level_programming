#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new = []
    for i in range(len(my_list) - 1):
        if i == idx:
            new.append(element)
        new.append(my_list[i])
    return new
