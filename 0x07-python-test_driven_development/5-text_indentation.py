#!/usr/bin/python3
''' separet a text in lines '''


def text_indentation(text):
    ''' a function that do str separation after each (.,?,:) by 2 lines.
    Args:
    @text: a text (str)

    Return: None
    '''

    if not isinstance(text, str) or isinstance(text, bool):
        raise TypeError('text must be a string')

    if text:
        start = 0
        sub = ''
        for i in range(len(text)):
            if text[i] in ['.', '?', ':']:
                sub = text[start:i + 1]
                sub = sub.strip()
                start = i + 1
                print(sub)
        print(text[start:].strip(), end='')
    else:
        print(end='')
