#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    length = len(names)
    for 1 in range(0, length):
        if names[i].startwith("_"):
            continue
        else:
            print("{}".format(names[i]))
