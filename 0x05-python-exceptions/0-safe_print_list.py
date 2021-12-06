#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    var = 0
    for elements in range(x):
        try:
            print(f"{my_list[elements]}", end="")
            var += 1
        except IndexError:
            break
    print()
    return var
