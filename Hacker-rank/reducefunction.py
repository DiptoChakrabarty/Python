a=[]
b=[]

for i in range(len(fracs)):
    a.append(fracs[i].numerator)
    b.append(fracs[i].denominator)
    
l=reduce(lambda x,y:x*y ,a)
m=reduce(lambda x,y:x*y ,b)
t=Fraction(l,m)
print(t.numerator, t.denominator)
