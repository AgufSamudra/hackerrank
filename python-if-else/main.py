#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    # if even and range beetwend 2 to 5
    if (n % 2 == 0) and (n in range(2, 6)):
        print("Not Weird")
    
    # if even and range beetwend 6 to 20
    elif (n % 2 == 0) and (n in range(6, 21)):
        print("Weird")
    
    # if even and greater than 20
    elif (n % 2 == 0) and (n > 20):
        print("Not Weird")
    
    # if odd
    elif (n % 2 != 0):
        print("Weird")
