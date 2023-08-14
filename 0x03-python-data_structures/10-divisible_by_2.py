#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_str = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            new_str.append(True)
        else:
            new_str.append(False)
    return (new_str)
