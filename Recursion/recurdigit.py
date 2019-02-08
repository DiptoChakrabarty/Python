def rev(n):
    s=0
    if(n>=1):
        
        s=s+(n%10)+rev(n//10)
        print(s)
        
    return s

n=int(input())
k=rev(n)
print("*",k)
        
        
        
