#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return 0, None
    new = sentence.split(" ")
    return len(new[0]), new[0][0]
