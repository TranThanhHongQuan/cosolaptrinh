import math
def LaSoNguyenTo(x):
    if x < 2:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
def SoHopLe(x):
    if x <= 1:
        return True
    else:
        return False
def NhapVaDem():
    a = 0
    print("Nhap day so:")
    while True:
        x = int(input(""))
        if SoHopLe(x):
            break
        if LaSoNguyenTo(x):
            a+= 1
    return a
def InKQ(kq):
    print("Co",kq,"so nguyen to")
kq = NhapVaDem()
InKQ(kq)
