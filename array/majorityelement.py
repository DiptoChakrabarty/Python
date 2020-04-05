https://www.geeksforgeeks.org/majority-element/
def maxelement(l):
    maxel=0
    count=1
    for i in range(len(l)):
        if l[maxel]==l[i]:
            count+=1
        else:
            count-=1
        if count==0:
            maxel=i
            count=1
    return l[maxel]

def half(l,n):
    count=0
    for i in range(len(l)):
        if n==l[i]:
            count+=1
    if count > len(l)/2:
        return True
    else:
        return False

def showelement(l):
    n =maxelement(l)
    if half(l,n):
        print(n)
    else:
        print(-1)

t = int(input())
for k in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    showelement(l)

                
