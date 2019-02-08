def missingNumbers(a, b):
    r=set(b)
    print(r)
    l=[]
    for i in range(len(b)):
        if b[i] not in a:
            print(b[i])
            l.append(b[i])
    for i in r:
        print(i)
        print(a.count(i),b.count(i))
        if(a.count(i)!=b.count(i)):
            
            l.append(i)
    l=set(l)
    l=list(l)
    l.sort()
    return l

arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))
result=missingNumbers(arr, brr)
print(result)
