#!/usr/bin/python3


def weight_average(my_list=[]):
    average = 0
    total_aver_num = 0
    if not len(my_list):
        return 0
    for num in my_list:
        average += num[0] * num[1]
        total_aver_num += num[1]
    return (average / total_aver_num)
