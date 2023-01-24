#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """A function that divides positional element of two lists

    Args:
        my_list_1 : first list
        my_list_2 : second list
        list_length : amount of division to be carried out
    return:
         a new list of divided elements
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
