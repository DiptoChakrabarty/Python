nm = input().split()
n = int(nm[0])
m = int(nm[1])
mt = []
for _ in range(n):
    matrix_item = input()
    mt.append(matrix_item)
p=0
print(mt)
k = int(input())
for i in range(n):
    for j in range(m):
        if(mt[i][j]=="M"):
            print(i,j)
            for i in range(n):
                for j in range(m):
                    print(i,j)
                    if(mt[i][j]=='x'):
                        p=p+1
                        if(mt[i+1][j]!='x' and i!=n):
                            i=i+1
                        elif(mt[i-1][j]!='x'):
                            i=i-1
                        elif(mt[i][j+1]!='x'):
                            j=j+1
                        if(mt[i][j-1]!='x'):
                            j=j+1
                    elif(mt[i][j]=='*'):
                        break
print(p)                       
if(p==k):
    print("g")
else:
    print("b")
                        
                    
            
            
