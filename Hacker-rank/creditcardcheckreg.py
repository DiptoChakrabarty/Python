import re
t=int(input())
for q in range(t):
    count=0
    n=input()
    
    l=len(n)
    
    if(l==16):
        if re.match("^[4-6][0-9]{15}",n):
            
            for r in range(15):
                if(n[r]==n[r+1]):
                    count=count+1
                    
                    if(count==3):
                        break
                else:
                    count=0
            
            if(count==3):
                print("Invalid")
                
            else:
                print("valid")
            

            
        
        else:
            print("Invalid1")
    elif(l==19):
        
        if re.match("^[4-6][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}",n):
            p=[]
            for i in range(l):
                
                if(n[i]!="-"):
                    p.append(n[i])
            
            for r in range(15):
                if(p[r]==p[r+1]):
                    count=count+1
                    if(count==3):
                        break
                else:
                    count=0
            if(count>=3):
                print("Invalid")
            else:
                print("valid")
        else:
            print("Invalid")
    else:
            print("Invalid")
        
