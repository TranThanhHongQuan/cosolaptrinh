def nhap():
    x=int(input("x="))
    L=[]
    n=int(input("n="))
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L,x
def search(L, x):
    for i in range(len(L)):
        if L[i] == x:
            return i
    return None
L,x=nhap()
a=search(L,x)
print("vi tri cua x trong L la:",a)
print(L)