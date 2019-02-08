#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def sort1(arr):
    
    p=[]
    p=arr
    p.sort()
    #print(p)
    for i in range(len(arr)):
            for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
                break
    if (arr==p):    
        print("YES",i,j+1)
    else:
        return 0

def almostSorted(arr):
    p=arr.sort()
    if(p==arr):
        print("yes")
    elif(p!=arr):
        t=sort1(arr)
        
        
        
            

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
