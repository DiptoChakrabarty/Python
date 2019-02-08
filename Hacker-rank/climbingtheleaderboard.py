s = list(map(int, input().rstrip().split()))
a = list(map(int, input().rstrip().split()))
l=[]
k=[]
for j in s:
    if j not in k:
        k.append(j)
print(k)
n=len(k)
print(n)

for j in a:
    print(j)
    print(l)
    if(j>k[0]):
        l.append(1)
        continue
    elif(j<k[n-1]):
         l.append(n+1)
         continue
    for i in range(n-1):
        print(k[i],k[i+1],i)
        if(k[i]>j and j>k[i+1]):
            l.append(i+2)
            break
        elif(j==k[i]):
            l.append(i+1)
            break
       
                
print(l)
