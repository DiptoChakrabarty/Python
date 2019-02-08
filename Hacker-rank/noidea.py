n,m=map(int,input().split())
c=0
print(n)
print(m)
t=set(map(int,input().split()))
print(t)
#for j in range(m):
#a=list(map(int,input().split()))
a=set(map(int,input().split()))
print(a)
#for j in range(m):
b=set(map(int,input().split()))
print(b)

z=a.intersection(t)
y=b.intersection(t)
print(len(z)-len(y))
