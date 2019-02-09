import numpy
numpy.set_printoptions(sign=' ')
n,m=map(int,input().split())
l=[]
for i in range(n):
    t=list(map(int,input().split()))
    l.append(t)
k=numpy.array(l)
#a=numpy.sum(l,axis=0)
print(numpy.mean(k,axis=1))
print(numpy.var(k,axis=0))
print(numpy.std(k))


