from itertools import combinations
n,k=input().split()
p=int(k)
s=[]

for m in range(1,p+1):
    l=list(combinations(sorted(n),m))#sorts string
    
    
    for i in l:
        d=list(i)
        d.sort()
        
        s.append(d)
        
        

for i in s:
    for j in range(len(i)):
        print(i[j],end='')
    print("")
