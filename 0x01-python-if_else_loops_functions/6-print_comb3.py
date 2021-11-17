#!/usr/bin/python3
for i in range(0, 10):
    for number in range(0, 10):
        if i >= number:
            continue
        elif i == 8 and number == 9:
            print("{}{}".format(i, number))
        else:
            print("{}{}, ".format(i, number), end='')
