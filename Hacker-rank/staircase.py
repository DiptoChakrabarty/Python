#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    t='#'
    r=' '
    for i in range(0,n):
        print(r*(n-i-1),t*(i+1))
'''def staircase(n):
    
    k = 2*n - 2
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # inner loop to handle number spaces 
        # values changing acc. to requirement 
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 2
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") '''

if __name__ == '__main__':
    n = int(input())

    staircase(n)

    
