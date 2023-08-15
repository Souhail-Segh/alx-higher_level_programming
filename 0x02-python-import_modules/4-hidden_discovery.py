#!/usr/bin/python3
import hidden_4
import inspect

if __name__ == '__main__':
    names = dir(hidden_4)
    for name in names:
        # Get the object for the name
        obj = getattr(hidden_4, name)
        # Check if the object is a function
        if inspect.isfunction(obj):
            if name != '__init__':
                print('{}'.format(name))
