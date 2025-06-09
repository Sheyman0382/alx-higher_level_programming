#!/usr/bin/python3


"""A module and indents a text accordingly"""


def text_indentation(text):
    """
    A function that indents a text accordingly
    Args:
        text(str): the text to be indented
    Raise:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    count = 0
    result = ""
    while count < len(text):
        result += text[count]
        if text[count] in ['.', '?', ':']:
            result += "\n\n"
            count += 1
            # skip any space after punctuation
            while count < len(text) and text[count] == " ":
                count += 1
            continue
            # prevents the next character from
            # being stripped off by the next line of code
        count += 1
