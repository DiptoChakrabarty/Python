def fibonacci(n):
    l=[0,1]
    s=0
    a=0
    b=1
    for i in range(n-2):
        s=a+b
        l.append(s)
        a=b
        b=s
    return l
n=int(input())
print(fibonacci(n))
