#!/usr/bin/python3
def uppercase(str):
    for i in str:
        cap = ord(i)
        if cap >= 97 and cap <= 122:
            cap = chr(cap - 32)
        else:
            cap = chr(cap)
        print("{}".format(cap), end="")
    print("")
