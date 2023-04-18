n=int(input("n="))
A=[]
B=[]
for i in range (1,n+1):
    x=int(input())
    A.append(x)
A.reverse() 
B=A.copy()
print(B)
B.sort()
print(B)