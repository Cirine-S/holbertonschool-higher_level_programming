#!/usr/bin/python3
'''
text_indentation
'''


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    for punct in ".?:":
        text = (punct + "\n\n").join(
            [i.strip(" ")for i in text.split(punct)])

    print(text, end="")
