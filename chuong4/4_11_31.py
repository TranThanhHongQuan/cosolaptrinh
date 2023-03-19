
import random

#may
def may():
        m=random.randint(1,3)
        print("may: ",m)
        if n==m:
            print("hoa")
        elif n==1 and m==2:
            print("nguoi thang")
        elif n==1 and m==3:
            print("may thang")
        elif n==2 and m==1:
            print("may thang")
        elif n==2 and m==3:
            print("nguoi thang")
        elif n==3 and m==1:
            print("nguoi thang")
        elif n==3 and m==2:
            print("may thang")
        return m
while True: 
#nguoi
    n=int(input("Nguoi: "))
    if n==0:
        break
    may()

#vong lap

