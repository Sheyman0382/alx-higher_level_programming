#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{}".format(i))
    else:
        print("{:0>2}".format(i), end=", ")
