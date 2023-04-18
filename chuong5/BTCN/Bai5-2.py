def Input():
    n=int(input("n="))
    L=[]
    for i in range (1,n+1):
        x=int(input())
        L=L+[x]
    return L
def Search(L):
    max=L[0]
    min=L[0]
    for i in range(1, len(L)):
        if L[i]>max:
            max = L[i]
        if L[i]<min:
            min = L[i]
    return max,min
def Output(max,min):
    print(max,min)
    return
L=Input()
max,min=Search(L)
Output(max, min)