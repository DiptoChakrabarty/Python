t=input()
u=[]
l=[]
e=[]
o=[]
for i in t:
    if(i.isalpha()==True):
        
        if(i.islower()==True):
            l.append(i)
        elif(i.islower()==False):
            u.append(i)
    elif(i.isdigit()==True):
        if(int(i)%2==0):
            e.append(i)
        else:
            o.append(i)
            
        
        
u.sort()
l.sort()
e.sort()
o.sort()
w=l+u+o+e
for j in w:
    print(j,end='')
            
