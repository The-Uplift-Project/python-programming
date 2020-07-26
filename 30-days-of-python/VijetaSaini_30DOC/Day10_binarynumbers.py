#Day Code
#Binary Numbers

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    count=0 
    m=0

    while(n>0):
        rem=int(n%2)
        if(rem==1):
            count+=1
        else:
            count=0
        if(count>=m):
            m=count
            
        n=n/2
 
    print(m)
        
        

