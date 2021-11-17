#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

LastDigit = abs(number) % 10
if number < 0:
    LastDigit = -LastDigit
print("Last digit of {} is {} and is".format(number, LastDigit), end=" ")
if LastDigit > 5:
    print("greater than 5")
elif LastDigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
