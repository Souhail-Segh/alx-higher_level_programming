#!/usr/bin/python3
'''Declaration of a Base Class '''


class Base:
    ''' A base Class.

    Initialisation of class variables:
        __nb_objects: private
        id
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Constructor methos '''
        self.__nb_objects = 0
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
