n=int(input("give range "))
l=[]

for i in range(n):
    t=int(input("give no "))
    l.append(t)


print(l)

for i in range(n):
    for j in range(i):
        if(l[i]>l[j]):
            l[i]=l[j]+l[i]
            l[j]=l[i]-l[j]
            l[i]=l[i]-l[j]


print(l)


            
            
        
        
    
