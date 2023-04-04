import math
def nhap():
    print("Nhap 3 so nguyen:")
    a=float(input("a="))
    b=float(input("b="))
    c=float(input("c="))
    return a,b,c
def giaipt(a,b,c):
    delta=b**2-4*a*c
    if delta==0:
        x1=x2=((-b)/2*a)
    elif delta>0:
        x1=(-b+math.sqrt(delta))/2*a
        x2=(-b-math.sqrt(delta))/2*a
    else:
        x1 = x2 = None
    return x1,x2
def inkq(x1,x2):
    if x1 == None and x2 == None:
        print("Phuong trinh vo nghiem")
    elif x1==x2:
        print("Phuong trinh co nghiem kep")
        print("x1=x2=",x1,sep="")
    else :
        print("Phuong trinh co hai nghiem")
        print("x1=",x1,sep="")
        print("x2=",x2,sep="")
a,b,c=nhap()
x1,x2=giaipt(a,b,c)
inkq(x1,x2)

        