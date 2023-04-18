n=int(input("n="))
A=[]
M=[]
for i in range (1,n+1):
    x=int(input())
    A=A+[x]
    if x not in A:
        M.append(x)
for x in M:
    print(x)

