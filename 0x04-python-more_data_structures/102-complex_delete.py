#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if value not in list(a_dictionary.values()):
        return a_dictionary
    for i in list(a_dictionary.keys()):
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
