n=int(input())
l=[]
count=0
for i in range(n):
    t=int(input())
    l.append(t)
    
k=len(l)
for j in range(k):
    if(l[j]%4!=0):
        
        
        for m in range(n-j):
            p=l[m-1]+l[j-1]
            if(p%4==0):
                count=count+1
                l.remove(l[m-1])
            
            
            
            
print(count)
