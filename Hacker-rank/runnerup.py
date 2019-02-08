n = int(input())

a=[int(x) for x in input().split()]

a.sort(reverse=True)

for i in range(n):
    if(a[i]!=a[0]):
        print(a[i])
        break
    
