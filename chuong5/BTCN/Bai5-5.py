n=int(input("n="))
A=[]
for i in range (1,n+1):
    x=int(input())
    A=A+[x]
    tong=0
for i in range(n):
    if i % 2 != 0 :
        tong+=A[i]
print("Tong=",tong,sep="")