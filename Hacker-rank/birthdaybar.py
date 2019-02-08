#!/bin/python3
from itertools import combinations
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    k=[]
    
    l=list(combinations(s,m))
    l=set(l)
    for i in l:
        
        if(sum(i)==d):
            print(i)
            k.append(i)
    t=set(k)
    return len(t)


    

n = int(input().strip())

s = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

d = int(dm[0])

m = int(dm[1])

result = birthday(s, d, m)

print(result)
