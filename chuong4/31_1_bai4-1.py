
def nhap():
    n=int(input("n="))
    print("nhap",n,"so nguyen")
    return n
def NhapVaDem(n):
    dem=0
    for i in range(n):
        b=int(input(""))
        if b%2==0 and b!=0:
            dem=dem+1
    return dem
def InKQ(kq):
    print("So chu so chan la:",kq)
n=nhap()
sochan=NhapVaDem(n)
InKQ(sochan)
            