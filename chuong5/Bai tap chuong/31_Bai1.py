def nhap():
    x=int(input())
    k=int(input())
    n=int(input())
    L=[]
    for i in range(1,n+1):
        y=int(input())
        L=L+[y]
    return L,x,k
def add(L,x,k):
    if k>(len(L)):
        L=L+[x]
    else:
        L=L[:k]+[x]+L[k:]
    return L
L,x,k=nhap()
print(add(L,x,k))
