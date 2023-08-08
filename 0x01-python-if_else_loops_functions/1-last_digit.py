#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_y = "Last digit of"
la_ty = abs(number) % 10

if la_ty > 5:
    print("{} {} is {} and is greater than 5".format(last_y, number, la_ty))
elif la_ty == 0:
    print("{} {} is {} and is 0".format(last_y, number, la_ty))
else:
    print("{} {} is {} and is less than 6 and not 0".format(last_y, number, la_ty))
