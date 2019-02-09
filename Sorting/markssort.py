def lsort(l):
    n=len(l)
    for i in range(n):
        for j in range(n-i-1):                    
            if(l[j]<l[j+1]):            
                l[j],l[j+1]=l[j+1],l[j]

    return l
'''def search(t,l):
    
        
    start=0
    end=len(l)
    while(start<end):
        
    
        mid=(start+end)//2
        p=l[mid]
        if(t==p):
            
            print(t)
            break
        elif(t>p):
            start=mid+1
        
        elif(t<p):
            end=mid-1
        
        else:
            print("not find")'''



n=int(input("give number of students "))
t=[]
l=[]
for i in range(n):
    a=input("give name ")
    b=int(input("give mark of student "))
    r=[a,b]
    t.append(b)
    l.append(r)

t=lsort(t)
for i in range(n):
    for j in range(n):
        if(t[i]==l[j][1]):
            print(l[j][0],end=' ')


