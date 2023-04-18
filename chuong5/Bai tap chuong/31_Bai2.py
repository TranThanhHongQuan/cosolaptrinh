def nhap():
    x=int(input())
    L=[]
    n=int(input())
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
print(a)
