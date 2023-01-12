#!/usr/bin/python3

def mul_tuple(yup):
    return yup[0] * yup[1]

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    tuple_mul = sum(list(map(mul_tuple, my_list)))
    weight = sum([i[1] for i in my_list])
    return tuple_mul / weight
