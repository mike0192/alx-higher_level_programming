#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    import sys
    operators = ["+", "-", "*", "/"]
    argv = sys.argv[1:]
    argv_boom = len(argv)
    if argv_boom != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        result = int(a, b)
        print("{} {} {}".format(a, operators, b))
