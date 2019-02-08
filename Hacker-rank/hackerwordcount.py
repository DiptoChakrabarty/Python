
string=input("give ")
k=int(input("give no "))
li=[]  
    # your code goes here    
l=len(string)
for i in range(0,l,k):
    r=string[i:i+k]
    if(len(r)==k):
        t=''
        for x in r:
            if x not in t:
                t=t+x
        li.append(t)
        r=''

print(li)
