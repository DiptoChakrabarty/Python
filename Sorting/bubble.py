#n=int(input("give range "))

#for i in range(n):
l=list(map(int,input().split()))
    
n=len(l)

print(l)

for i in range(n):
    for j in range(n-i-1):
        
        if(l[j]>l[j+1]):
            
            l[j],l[j+1]=l[j+1],l[j]
            

print(l)
