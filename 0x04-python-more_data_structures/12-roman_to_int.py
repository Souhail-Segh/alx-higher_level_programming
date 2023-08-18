#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        if isinstance(roman_string, str) is False:
            return 0
        sum = 0
        prev = ''
        roman = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for s in roman_string:
            if s in roman:
                sum += roman[s]
                if (s in ['V', 'X']) and (prev == 'I'):
                    sum -= 2
                elif (s in ['L', 'C'] and (prev == 'X')):
                    sum -= 20
                elif (s in ['D', 'M']) and (prev == 'C'):
                    sum -= 200
                prev = s
            else:
                return 0
        return sum
    return 0
