n=int(input())
l=list(map(int,input().split()))
p=set(l)
r=len(l)
s=(sum(p)*n)*sum(l)
print(s//(n-1))
