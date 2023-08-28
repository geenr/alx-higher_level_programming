#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    numb = 0
    for z in range(0, x):
        try:
            print("{:d}".format(my_list[z]), end="")
            numb += 1
        except (TypeError, ValueError):
            continue
    print()
    return (numb)
