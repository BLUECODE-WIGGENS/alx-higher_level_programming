#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    var = 0
    for elements in range(x):
        try:
            print("{:d}".format(my_list[elements]), end="")
            var += 1
        except IndexError:
            raise
        except:
            continue
    print()
    return var
