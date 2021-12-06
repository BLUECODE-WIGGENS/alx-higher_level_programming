#!/usr/bin/python3
def magic_calculation(a, b):
    bytecode = 0
    for elements in range(1, 3):
        try:
            if elements > a:
                raise Exception("Too many arguments")
            else:
                bytecode += (a**b) / elements
        except:
            bytecode = b + a
            break
    return bytecode
