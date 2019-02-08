nk = input().split()
n = int(nk[0])
k = int(nk[1])
r = int(input())
c = int(input())
o = []
z=0
for _ in range(k):
    o.append(list(map(int, input().rstrip().split())))
l=[]
p=[]
a=[]
for i in range(n):
    l=l+[0]
for i in range(n):
    l[i]=[0]*n
l[r-1][c-1]=1
for i in range(len(o)):
    l[o[i][0]-1][o[i][1]-1]=2
print(l)


for i in range(n):
    for j in range(n):
        if(l[i][j]==2):
            a.append(abs(r-i))
            p.append(abs(c-j))
print(a)
print(p)

for i in a:
    if(i>1):
        for j in range(i):
            z=z+j
            print(z)
for i in p:
    if(i>1):
        for j in range(i):
            z=z+j
            print(z)

print(z)            
            
        
