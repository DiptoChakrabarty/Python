import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    p=[]
    for i in range(len(arr)):
        j=sum(arr)-arr[i]
        p.append(j)
    return max(p),min(p)
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
