from itertools import combinations_with_replacement
l=list(map(int,input().split()))
n=int(input())
k=len(l)
d=[]
for i in range(k):
    t=list(combinations_with_replacement(l,i+1))
    d.append(t)

for i in range(len(d)):
    #if(sum(list(i))==n):
    for j in range(len(d[i])):
        if(n==(sum(d[i][j]))):
            print(list(d[i][j]))
    
