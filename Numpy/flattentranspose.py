import numpy
l=[]
r=list(map(int,input().split()))
n=r[0]
m=r[1]
for i in range(n):
    k=list(map(int,input().split()))
    l.append(k)
a=numpy.array(l)
print (numpy.transpose(a))
#gives transpose of nested list elements
print (a.flatten())
#makes whole nested arrays into one single array



