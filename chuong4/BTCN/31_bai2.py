def nhap():
    n=int(input("n="))
    return n
def inkq(n):
    if n>=2:
        for i in range(2,n+1,2):
            print(i,end=" ")
        print()
while True:
    n=nhap()
    i=inkq(n)
    d=str(input("Tiep tuc khong?"))
    if d=="k" or d=="K":
        break
    

        