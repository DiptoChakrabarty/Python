#n=int(input("give no "))
a=[4,5,1,0,3,6,4]
count=7
r=0
#for i in range(n):
 #   a[i]=int(input("give no ",i))
  #  count=count+1

print(a)

t=int(input("give no to be found "))
for i in range(n):
    if (t==a[i]):
        r=r+1


print(r/count)
