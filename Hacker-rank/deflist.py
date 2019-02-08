def maxlist(l):
    max=0
    for i in range(len(l)):
        if(l[i]>max):
            max=l[i]


    return max
w=[]
n=int(input("give no "))
for j in range(n):
    t=int(input())
    w.append(t)

print(maxlist(w))
    

