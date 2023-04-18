def nhap():
    x=int(input("x="))
    k=int(input("k="))
    n=int(input("n="))
    L=[]
    for i in range(1,n+1):
        y=int(input("y="))
        L=L+[y]
    return L,x,k
def add(L,x,k):
    if k>(len(L)):
        L=L+[x]
    else:
        L[k]=x
    return L
def  InKQ(L):
    print(L)
L,x,k=nhap()
L=add(L,x,k)
InKQ(L)