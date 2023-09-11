#!/usr/bin/python3
'''
Class about sorting a list
'''


class MyList(list):
    ''' Subclass of a list '''
    def  __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
