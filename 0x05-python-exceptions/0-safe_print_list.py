#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    text = ""
    try:
        for i in range(x):
            text += str(my_list[i])
        print(text)
        return x
    except:
        sum = 0
        for i in my_list:
            sum += 1
        print(text)
        return sum
