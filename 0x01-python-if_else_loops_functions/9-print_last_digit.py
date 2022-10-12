#!/usr/bin/python3
def print_last_digit(number):
    ldigit = int(str(number)[-1])
    print("{}".format(ldigit), end="")
    return(ldigit)
