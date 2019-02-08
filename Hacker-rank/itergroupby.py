from itertools import groupby
s=input()
l=[]
for i,j in groupby(s):
    #print(len(list(j),i))
    l.append((len(list(j)),int(i)))

for k in l:
    print(k,end=' ')
