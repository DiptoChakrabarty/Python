s=input("give ")
l=len(s)
r=[]
g=[]


for i in range(l):
    t=s[i]
    c=1
    for j in range(i+1,l):
        if(t==s[j]):
            c=c+1
    if(c>1):    
        a=[c,t]
        g.append(c)
        
        r.append(a)

q=''
r.sort(reverse=True)
g.sort(reverse=True)
print(r)
p=len(r)
for i in range(p-1):
    if r[i][1] not in q:
        
        q=q+r[i][1]
        for j in range(i+1,p):
            if(r[i][0]==r[j][0]):
                if( ord(r[i][1])<ord(r[j][1])):
                    print(r[i][1],r[i][0])
                    print(r[j][1],r[j][0])
                else:
                    print(r[j][1],r[j][0])
                    print(r[i][1],r[i][0])
            else:
                print(r[i][1],r[i][0])
                break
print(q) 
                    
    
        
        
