n= int(input())
b= list(map(int, input().rstrip().split()))
l=[]
p=0
k=0
l=b
print(b)
print(l)

for i in range(n):
    for j in range(n-1,i-1,-1):
        if(l[j]<l[i]):
            l[j],l[i]=l[i],l[j]
            p=p+1

for i in range(n):
        for j in range(n-1,i-1,-1):
            if(b[j]>b[i]):
                b[j],b[i]=b[i],b[j]
                k=k+1
print(l)
print(p,k)
