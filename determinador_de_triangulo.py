ds=str(input("Digite os 3 valores separados por virgula"))
d=ds.split(",")


a=d[0]
b=d[1]
c=d[2]


if a==b and b==c:
    print("equilatero")
    
elif a!=b and b!=c and c!=a:
    print("escaleno")
    
else:
    print("isosceles")
