x=int(input("no 1 "))
y=int(input("no 2 "))
def pow(x,y):
    if y!=0:
        return(x*pow(x,y-1))
    else:
        return 1
print(pow(x,y))
