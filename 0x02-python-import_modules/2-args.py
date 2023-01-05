#!/usr/bin/python3
import sys
if __name__ == "__main__":

    args_count = len(sys.argv) - 1
    if args_count == 0:
        print("0 arguments")
    elif args_count == 1:
        print("1 argument")
    else:
        print("{} arguments".format(args_count))
    for ind in range(args_count):
        print("{}: {}".format(ind + 1, sys.argv[ind + 1]))
