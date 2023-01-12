#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary):
        return None
    name = list(dict(sorted(a_dictionary.items(), key=lambda
                            item: item[1])).keys())[-1]
    return name
