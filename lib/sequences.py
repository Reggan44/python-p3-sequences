#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    elif length == 2:
        print([0, 1])
        return
    else:
        fibs = [0, 1]
        for i in range(2, length):
            fibs.append(fibs[-1] + fibs[-2])
        print(fibs)