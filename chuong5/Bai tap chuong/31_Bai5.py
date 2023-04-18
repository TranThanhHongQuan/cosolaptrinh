def nhap():
    x=int(input("x="))
    y=int(input("y="))
    L=[]
    n=int(input("n="))
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L,x,y
def replace(L, x, y):
    for i in range(len(L)):
        if L[i] == x:
            L[i] = y   
    return L
L,x,y=nhap()
replace(L,x,y)
print(L)