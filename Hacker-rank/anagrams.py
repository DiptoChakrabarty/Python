from itertools import permutations
t=int(input())
for i in range(t):
    a=input()
    b=input()
    l=set(permutations(a,len(a)))
    q=set(permutations(b,len(b)))
    print(l)
    print(q)
    z=[]
    z.append(len(l))
    z.append(len(q))
    print(min(z))
