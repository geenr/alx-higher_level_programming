#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    no_of_argvss = len(sys.argv) - 1

    if no_of_argvss == 0:
        print("0 arguments.")
    elif no_of_argvss == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(no_of_argvss))
    for c in range(no_of_argvss):
        print("{}: {}".format(c + 1, sys.argv[c + 1]))
