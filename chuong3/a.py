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
#       break
for i in range(1,10):
    for j in range(1,10):
        print(str(i*j).rjust(4),end=" ")
    print()


