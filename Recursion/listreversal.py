def reverse(l,a):
    n=len(l)
    if(a>0):
        k=l[a-1]
        l.append(k)
        reverse(l,a-1)    
    return l
l=list(map(int,input().split()))
c=len(l)
k=reverse(l,c)
print(k[c:])
