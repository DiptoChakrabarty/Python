n=int(input())
l=[]
k=[]
e=[]
for i in range (n):
    t=input()
    l.append(t)
print(l)
for j in l:
    if j not in k:
        k.append(j)
print(k)
print(len(k))

    
for m in range(len(k)):
    c=0
    for d in l:
        if( k[m]==d):
            c=c+1
    e.append(c)


print(e)
for i in e:
    print(i,end=' ')
        
            
    
        
    

