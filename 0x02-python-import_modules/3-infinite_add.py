#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    argv = sys.argv
    length = len(argv)
    for i in range(1, length):
        count = count + int(argv[i])
    print("{}".format(count))
