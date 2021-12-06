#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    var = []
    for elements in range(list_length):
        try:
            division = my_list_1[elements] / my_list_2[elements]
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except (TypeError, ValueError):
            print("wrong type")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            var.append(division)
    return var
