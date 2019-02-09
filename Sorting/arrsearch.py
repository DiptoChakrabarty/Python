n=int(input("give range "))
l=[]
p=0
for i in range(n):
    t=int(input("give no "))
    l.append(t)
t=int(input("give no to be searched "))


print(l)

for i in range(n):
    if( l[i]==t):
        print("found at position ",i+1)
        p=p+1
if(p==0):
    print("not found")
    
