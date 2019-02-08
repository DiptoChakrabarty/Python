li=[]
string="AABCAAADA"
k=3
    # your code goes here    
p=len(string)
print(p)

for i in range(0,p,k):
    r=string[i:i+k]
    #print(r)
    if(len(r)==k):
        
        li.append(r)
        r=""
for j in li:    
    t=[j]
    for q in range(k):
        for y in range(q):
    
