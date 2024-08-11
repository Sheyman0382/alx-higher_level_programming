#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = number % -10
        num = num * - 1
    else:
        num = number % 10
    print(num, end="")
    return(num)
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
