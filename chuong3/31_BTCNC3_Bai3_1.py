import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
p=(a+b+c)/2
if (a+b)>c and (a+c)>b and (b+c)>a:
    dientich=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich=",round(dientich,3),sep="")
else:
    print("Khong hop le")
    

