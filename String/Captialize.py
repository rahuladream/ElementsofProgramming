"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.

"""



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    print(s.title().join(s.split()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
