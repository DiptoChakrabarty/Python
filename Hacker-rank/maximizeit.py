from itertools import product
def sqr(l):
    for i in range(len(l)):
        
        l[i]=l[i]**2
    return l
A=list(map(int,input().split()))
max=0
l=[]
p=[]
z=[]
k=A[0]
m=A[1]
for i in range(k):
    a=list(map(int,input().split()))
    a.pop(0)
    p=sqr(a)
    l.append(p)

b=list(product(*l))
for i in b:
    t=sum(i)%m
    z.append(t)
z.sort() 
print(z[-1])
    

