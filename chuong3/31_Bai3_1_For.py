n=int(input("n="))
for n in range(1,50): 
    if n%10==1:
        print()
    elif n==46:
        break
    print(n,end=" ")
    