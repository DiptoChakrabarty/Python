def superDigit(n, k):
    l=list(n)
    s=0
    for i in l:
        s=s+int(i)
    t=s*k
    if((t//10)>0):
        p=sum0(t)
        return sum0(p)

def sum0(t):
    k=0

    if(t//10==0):
        return t
    else:
        return (t%10+sum0(t//10))


w=int(input())
a=int(input())
k=superDigit(w,a)
print(k)
