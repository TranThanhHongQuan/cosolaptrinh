import math
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
s=(a+b+c)/2
Dt=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Dientich:",Dt)