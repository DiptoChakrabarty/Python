import numpy
'''a=list(map(int,input().split()))
n=a[0]
m=a[1]
print( numpy.eye(n, m))'''
import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))


#helps make identity matrices
