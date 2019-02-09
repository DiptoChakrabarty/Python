l=list(map(int,input().split()))
n=len(l)
l.sort()
print(l)
r=int(input("give element "))
'''if(n%2==0):
    start=0
    end=n
else:
    start=0
    end=n+1'''
start=0
end=n
while(start<end):
    
    mid=(start+end)//2
    p=l[mid]
    if(r==p):
        print("found at pos",mid ," ",l[mid])
        break
    elif(r>p):
        start=mid+1
        
    elif(r<p):
        end=mid-1
        
    else:
        print("not find")
