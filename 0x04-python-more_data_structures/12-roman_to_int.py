#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        roman_const = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,
                       'X': 10, 'V': 5, 'I': 1}
        sub_roman_string = {
            'CM': 900,
            'CD': 400,
            'XC': 90,
            'XL': 40,
            'IX': 9,
            'IV': 4}
        result = 0
        for item in sub_roman_string.keys():
            if item in roman_string:
                roman_string = roman_string.split(item)
                roman_string = "".join(roman_string)
                result += sub_roman_string[item]
        for i in roman_string:
            result += roman_const[i]
        return result
    else:
        return 0
