from itertools import combinations
n=int(input())
p=0
t=[]
#t=list(map(input().split()))
a=input()
for i in a:
    if(i!=" "):
        t.append(i)
k=int(input())
l=list(combinations(t,k))
for i in range(len(l)):
    for j in range(len(l[i])):
        if(l[i][j]=="a"):
            p=p+1
            break
            
s=len(l)
print(p/s)
        
