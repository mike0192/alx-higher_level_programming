#!/usr/bin/env python3
def no_c(my_string):
    breezy = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            breezy += i
    return breezy
