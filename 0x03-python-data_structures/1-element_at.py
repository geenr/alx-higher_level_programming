#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in range(len(my_list)):
        if idx > len(my_list):
            return None
        elif idx < 0:
            return None
        else:
            print("{}".format(my_list[idx]))
