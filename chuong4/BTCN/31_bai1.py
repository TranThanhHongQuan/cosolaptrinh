def nhap():
    n=int(input("n="))
    return n
def giathua(n):
    gt=1
    for i in range(1,n+1):
        gt=gt*i
    return gt
def inkq(n,X):
    print(n,"!=",X,sep="")
n=nhap()
X=giathua(n)
inkq(n,X)
