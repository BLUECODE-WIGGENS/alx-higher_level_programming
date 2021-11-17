#!/usr/bin/python3
n = 0
for i in range(1, 101, 10):
    for number in range(i, i + 9):
        if number > n:
            print("{:02}".format(number), end='')
            if number < 88:
                print(', ', end='')
    n += 11
    print()
