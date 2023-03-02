import math
print("Nhap hai canh ke cua tam giac vuong:")
A=int(input())
B=int(input())
canhhuyen=math.sqrt(A**2+B**2)
print("Canh ke thu nhat la:",A,end=(","))
print(" canh ke thu hai:",B,end=(","))
print(" co canh huyen =",round(canhhuyen,2))
