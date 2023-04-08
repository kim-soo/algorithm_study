#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'paperCuttings' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER textLength
#  2. INTEGER_ARRAY starting
#  3. INTEGER_ARRAY ending
#

def paperCuttings(textLength, starting, ending):
    # Write your code here
    for i in starting:
        if i is not None :
            for j in range((i+1), len(starting)):
                if ((starting[i] == starting[j]) and (ending[i] == ending[j])):
                    del starting[j], ending[j]
    result = 0
    for i in range(len(starting)):
        if starting[i] is not None and ending[i] is not None:
            array=[]
            num = starting[i]
            while num <= ending[i]:
                array.append(num)
                num = num + 1
            print(array)
            for j in range((i+1), len(starting)):
                answer = True
                num2 = starting[j]
                while num2 <= ending[j]:
                    if num2 in array:
                        answer = False
                        break
                    else:
                        num2 = num2 + 1
                if answer == True:
                    result = result + 1
        array.clear()
    return result

    
if __name__ == '__main__':

    textLength = 10
    starting = [3,1,2,8,8]
    ending = [5,3,7,10,10]

    result = paperCuttings(textLength, starting, ending)
    print(result)