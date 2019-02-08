def icecreamParlor(m,l):
    n=len(l)
    for i in range(n):
        s=0
        for j in range(n):
            s=l[i]+l[j]
            print(s)
            if(s==m and i!=j):
                return i+1,j+1
                break
    

m=int(input("give "))
arr = list(map(int, input().rstrip().split()))
print(arr)
t=icecreamParlor(m,arr)
print(t)
