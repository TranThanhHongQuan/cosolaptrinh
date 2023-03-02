a=input("Ho ten: ")
b=int(input("So ngay cong: "))
c=int(input("Don gia ngay cong: "))
d=float(input("He so phu cap: "))
e=int(input("Tam ung: "))
Luong=c*b*d
Thuclinh=Luong-e

print("Nhan vien",a,end=(", "))
print("Co tien Luong=",round(Luong,1),sep="",end=(", "))
print("Tam ung=",e,sep="",end=(""))
print(" va Thuc linh=",round(Thuclinh,1),sep="")

