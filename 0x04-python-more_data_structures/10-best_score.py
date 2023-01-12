#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or a_dictionary is None:
        return None
    name = list(dict(sorted(a_dictionary.items(), key=lambda
                            item: item[1])).keys())[-1]
    return name
