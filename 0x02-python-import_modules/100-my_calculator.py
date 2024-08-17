#!/usr/bin/python3
import sys
import calculator_1 as calc
if __name__ == "__main__":
    argv = sys.argv
    length = len(argv)
    if length < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif length > 4:
        operator = "*"
        b = int(argv[length - 1])
    else:
        operator = argv[2]
    b = int(argv[length - 1])
    a = int(argv[1])

    if operator == "+":
        print("{} + {} = {}".format(a, b, calc.add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    elif operator == "/":
        print("{} / {} = {:.2f}".format(a, b, float(calc.div(a, b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
