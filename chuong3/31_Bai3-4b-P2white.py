i=1#cach1
n=9
while i<=n:
    print(' '*(n-i)+'*'*(2*i-1),end='')
    print()
    i=i+1
# cach2
i=1
n=int(input("n="))
while i<=n:
    print(" "*((n-i)//2),end="")
    print("*"*(i))
    i=i+2
print()