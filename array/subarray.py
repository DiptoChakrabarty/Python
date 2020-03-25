
#code
def check(s,l):
    curr = l[0]
    start = 0
    i=1
    n=len(l)
    while(i<=n):
        while curr > s and i-1> start:
            curr =curr - l[start]
            start = start+1
        if curr==s:
            print (start+1,i)
            return 1
        if i<n:
            curr = curr+l[i]
        i=i+1
    print(-1)
    return 0
        
        
    return 0
t= int(input())
for i in range(t):
    n,s = list(map(int,input().split()))
    l = list(map(int,input().split()))
    check(s,l)
    
    
