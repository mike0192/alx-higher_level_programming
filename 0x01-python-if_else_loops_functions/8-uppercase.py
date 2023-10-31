#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord("A") <= ord(str) <= ord("Z"):
            i = hcr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print() 
