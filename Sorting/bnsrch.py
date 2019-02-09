def srch(l,start,end,r):
    if(end>=1):
        mid=(start+end)//2
        if(l[mid]==r):
            print(l[mid],start,end)
            return mid
        elif(l[mid]>r):
            return srch(start,mid-1,r)
        elif(l[mid]<r):
            return (mid+1,end,r)
    else:
        return -1
l=list(map(int,input().split()))
n=len(l)
l.sort()
r=int(input())
start=0
end=n

k=srch(l,start,end-1,r)
print(k)
