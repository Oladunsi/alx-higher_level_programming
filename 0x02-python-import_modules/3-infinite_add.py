#!/usr/bin/python3
import sys
if __name__ == "__main__":

    args_count = len(sys.argv) - 1
    inf_sum = 0
    if args_count == 0:
        print("0")
    for ind in range(args_count):
        inf_sum += int(sys.argv[ind + 1])
    print("{}".format(inf_sum))
