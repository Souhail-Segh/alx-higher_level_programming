#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lt = []
    for i in range(2):
        a = b = 0
        if tuple_a:
           if len(tuple_a) > i:
               a = tuple_a[i]
        if tuple_b:
            if len(tuple_b) > i:
                b = tuple_b[i]
        lt.append(a + b)
    return (tuple(lt))
    
        
