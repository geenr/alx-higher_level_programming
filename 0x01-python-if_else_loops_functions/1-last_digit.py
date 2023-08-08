#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_y = "Last digit of"
la_ty = abs(number) % 10

if la_ty > 5:
    print(f"{last_y} {number} is {la_ty} and is greater than 5")
elif la_ty == 0:
    print(f"{last_y} {number} is {la_ty} and is 0")
else:
    print(f"{last_y} {number} is {la_ty} and is less than 6 and not 0")
