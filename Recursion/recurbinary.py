'''def fu2(n):
    if(n==0):
        return
    fu2(n/2)
    print(n%2)'''
'''def fun1(n):
    i=0
    if(n>3):
        fun1(n-1)
    for i in range(n):
        print(i,end=" ")'''
'''def fun(n):
    if(n<=0):
        return
    elif(n>100):
        return
    print(n)
    fun(2*n)
    print(n)'''
def max0(l,n):
    
    if(n==1):
        return l[0]
    else:
        k=max0(l,n-1)
        print(k,l[n-1])
    if(k>l[n-1]):
        return k;
    else:
        return l[n-1]
    
        
n=list(map(int,input().split()))
t=max0(n,len(n))
print("*",t)

