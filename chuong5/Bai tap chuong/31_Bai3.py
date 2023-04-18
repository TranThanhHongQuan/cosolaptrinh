def nhap():
    x=int(input())
    L=[]
    n=int(input())
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L,x
def delete(L,x):
    L1 = []
    for i in L:
        if i!= x:
            L1=L1+[i]
    return L1
L,x=nhap()
m=delete(L,x)
print(m)