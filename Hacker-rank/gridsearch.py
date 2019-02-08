t = int(input())

for t_itr in range(t):
    RC = input().split()

    R = int(RC[0])
    C = int(RC[1])
    G = []

    for _ in range(R):
        G_item = input()
        G.append(G_item)

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    P = []

    for _ in range(r):
        P_item = input()
        P.append(P_item)
print(G)
print(P)

l=len(P[0])
k=len(P)
c=0
for i in range(len(G)):
    t=G[i]
    print(t)
    for j in range(len(t)-l):
        r=t[j:j+l]
        print(r)
        if r in P:
            c=c+1
            break
if(c==k ):
    print( "YES")
elif(c<k):
    print("NO")
