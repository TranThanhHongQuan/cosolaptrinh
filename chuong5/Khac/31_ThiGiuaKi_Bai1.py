A=int(input())
B=int(input())
c=0
if A>0 and B>0 and A<=B:
    for i in range(A+1,B+1):
        c=c+i  
print(c)