def nhap():
    L=[]
    n=int(input("n="))
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L
def count(L):
    dem=0
    for i in L:
        dem=dem+1
    return dem
L=nhap()
c=count(L)
print("so cac phan tu trong list la:",c)
print(L)