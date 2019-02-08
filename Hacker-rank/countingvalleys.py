#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
'''def countingValleys(n, s):
    
    for i in range(n):
        if((s[i]=='D' and s[i-1]=='U')):
            c=0
            for j in range(i+1,n):
                if(s[j]=='D'):
                    c=c+1
                    
                elif(s[j]=='U'):
                    break
            if(c>=1):
                p=p+1
        elif(s[0]=='D'):
            if((s[i]=='D' and s[i-1]=='U')):
            c=0
            for j in range(i+1,n):
                if(s[j]=='D'):
                    c=c+1
                    
                elif(s[j]=='U'):
                    break
            if(c>=1):
                p=p+1
                
    return p'''

n=int(input("give range "))
l=list(map(int,input().split()))
for i in range(n):
    
    












