# num= 13
# if num< 0:
#      print ("The number is negative")
# elif num% 2 == 0 :
#      print ("The number is even")
# else:
#      print ("The number is odd")

# yrsorservice= int(input('so nam='))
# salary = int(input('salary='))
# bonus = 0
# if yrsorservice < 5:
#     if salary < 500:
#         bonus = 100

#     else:
#         bonus = 200
# else:
#     bonus = 700
# print ("Bonus amount: ", bonus)
# i=int(input('i='))
# n=1
# s=0
# while n<=i:
#     s+=n
#     n+=1
# print("tong=",s)
# while True:
#    n=int(input("n="))
#    if n<=0:
#      print("Khong hop le!!!\nMoi nhap lai")
#    else:
#       print("Hop le nhe!!!")
#       break
# # for i in range(1,10):
#     for j in range(1,10):
#         print(str(i*j).rjust(4),end=" ")
#     print()
# i=2
# while i<=10:
#     print(i)
#     i=i+2

# n=int(input("Nhap so nguyen: "))
# i=2
# S=0
# while i<=n:
#    S=S+i
#    i=i+2
# print("Tong S=",S)

#kim tu thap lech trai
# i=1
# n=10
# while i<=n:
#     print(" " * (n-i),end="")
#     print("*"*i)
#     i+=1
# #kim tu thap lech phai
# i=1
# n=10
# while i<=n:
#     print("*"*i,end="")
#     print(" "*(n-i))
#     i+=1
# i=1
# n=int(input("n="))
# while i<=n:
#     print(" "*((n-i)//2),end="")
#     print("*"*(i))
#     i=i+2
# print("\n")

# S=0
# n=int(input("Nhap n="))

# for i in range(1,n+1):
#     print("So thu ",i,": ",sep="",end="")
#     x=int(input())
#     if x<0:
#         continue
#     elif x==0:
#         break
#     else:
#         S=S+x
# print("S=",S,sep="")
# n=int(input("Nhap n="))
# i=1
# while i<=n:
#     print((n+1-i)*"%",end="")
#     print("")
#     i+=1

# n=6
# for i in range(1,n+1):
#     print(" ","*"*i,sep="")
#     print()

# char=input()
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(char,end=" ")
#         j+=1
#     print()
#     i+=1
    

#tro choi keo bua bao
# import random

# #may
# def may():
#         m=random.randint(1,3)
#         print("may: ",m)
#         if n==m:
#             print("hoa")
#         elif n==1 and m==2:
#             print("nguoi thang")
#         elif n==1 and m==3:
#             print("may thang")
#         elif n==2 and m==1:
#             print("may thang")
#         elif n==2 and m==3:
#             print("nguoi thang")
#         elif n==3 and m==1:
#             print("nguoi thang")
#         elif n==3 and m==2:
#             print("may thang")
#         return m
# while True: 
# #nguoi
#     n=int(input("Nguoi: "))
#     if n==0:
#         break
#     may()


