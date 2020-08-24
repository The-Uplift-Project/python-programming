#Day 28 Code
#Regular Expressions,Patterns and Intro to Databases


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    name_list=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if re.search('@gmail\.com$',emailID):
            name_list.append(firstName)
    print(*sorted(name_list),sep='\n')
