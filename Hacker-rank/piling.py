t=int(input())
for j in range(t):
    p=0
    
    
    n=int(input())
    l=list(map(int,input().split()))
    if(n%2!=0):
        k=n+1
    else:
        k=n
    print(l)
    m=k//2
    print(l.sort())
    l.sort(reverse=True)
    
    
    
        


    '''if( l[i]>l[i+1]):
         p=p+1
         print(p, " " ,l[j])
     elif(l[n-i-1]>l[n-i-2]):
        p=p+1
        print(p, " " ,l[j])'''

    print(p)
    if(p==n or v==n):
        print("Yes")
    else:
        print("No")
        
