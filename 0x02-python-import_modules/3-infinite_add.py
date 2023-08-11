#!/usr/bin/python3
if  __name__ == "__main__":
    import sys

    num_ber = sys.argv[1:]

    my_sum = sum(int(i) for i in num_ber)
    print("{}".format(my_sum))
