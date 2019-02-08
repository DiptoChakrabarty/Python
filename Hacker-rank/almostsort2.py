l = list(map(int, input().rstrip().split()))
print(l)

p=[]
    p=l
    p.sort()
    n=len(l)
    for i in range(n):        
        for j in range(n-i-1):        
            if(l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]
                break
    if (l==p):    
        print("yes")
        print("swap",j+1,j+2)
    
    k=[]
    for i in range(n):
        for j in range(i+1,n):
            if(l[i]>l[j]):
                k.append(l[i])
            else:
                break
    a=[]
    a=k

    if(k.sort()==a.reverse()):
    #print("YES",arr.index(k[0]),arr.index(k[len(k)]))
        print("YES")
    else:
        print("NO")
          
        
