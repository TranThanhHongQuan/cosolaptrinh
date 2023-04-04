# def intho(causo):
    
#     Loibaihat = ("A partridge in a pear tree.",
#         "Two turtle doves,",
#         "Three French hens,",
#         "Four calling birds,",
#         "Five golden rings,",
#         "Six geese a-laying,",
#         "Seven swans a-swimming,",
#         "Eight maids a-milking,",
#         "Nine ladies dancing,",
#         "Ten lords a-leaping,",
#         "Eleven pipers piping,",
#         "Twelve drummers drumming,")
    
    
#     sothutu = ("first", "second", "third", "fourth", "fifth", "sixth","seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth")
    
    
#     print(f"On the (sothutu(causo-1)) day of Christmas\nmy true love sent to me:")
#     for i in range(causo-1, 0, -1):
#         print(Loibaihat[i])
#     if causo > 1:
#         print("And", end=" ")
#     print(Loibaihat[0])
#     print()


# for i in range(1, 13):
#     intho(i)
#bài87
# def chuoikitu(n, chieurong):
#     demso = len(n)
#     if demso >= chieurong:
#         return n
#     padding = " " * ((chieurong - demso) // 2)
#     return padding + n
# def main():
#     n = input("n=")
#     chieurong = int(input())
#     chuoikitu = chuoikitu(n, chieurong)
#     print(chuoikitu)

# if __name__ == '__main__':
#     main()

# bài 100
# def Xacdinhngay():
#     thang=int(input("thang: "))
#     nam=int(input("nam: "))
#     return thang,nam
# def ktra(thang,nam):
#     if thang==2:
#         if nam % 4 == 0 : return 29
#         else : return 28
#     elif thang in (4,6,9,11):
#         return 30
#     else:return 31    
# def inramanhinh(inn):
#     print("Thang",thang,"Nam",nam,"co",inn,"Ngay")
# thang,nam=Xacdinhngay()
# ngay=ktra(thang,nam)
# inramanhinh(ngay)

#bai 103
# def ngaykidieu(ngay,thang,nam):
#     haisocuoicuanam=nam%100
#     return ngay*thang==haisocuoicuanam
# for nam in range(1900,2001):
#     for thang in range(1, 13):
#         ngaytrongthang=  31 if thang in(1,3,5,7,8,10,12) else \
#                         30 if thang in(4,6,9,11) else \
#                         29 if nam%4==0  else \
#                         28
#         for ngay in range(1,ngaytrongthang+1):
#             if ngaykidieu(ngay,thang,nam):
#                 print(ngay,"/",thang,"/",nam,sep="")
#bai91
# def uutien():
#     n = input("")
#     return n
# def toantu(n):
#     if n=="+" or n=="-":
#         print("1")
#     elif n=="*" or n=="/":
#         print("2")
#     elif n==("^"):
#         print("3")
#     else:print("-1")
# n=uutien()
# toantu(n)
#bài 95
# import random
# def taobiensoxe():
#     if random.random()<0.5:
#         a=random.randint(0,9)
#         b=random.randint(0,9)
#         c=random.randint(0,9)
#         d=random.randint(0,9)
#         a1=random.choice("qwertyuiopasdfghjklzxcvbnm")
#         a2=random.choice("qwertyuiopasdfghjklzxcvbnm")
#         a3=random.choice("qwertyuiopasdfghjklzxcvbnm")
#         print(a,b,c,d,a1,a2,a3,sep="")
#     else:
#         a=random.randint(0,9)
#         b=random.randint(0,9)
#         c=random.randint(0,9)
#         a1=random.choice("qwertyuiopasdfghjklzxcvbnm")
#         a2=random.choice("qwertyuiopasdfghjklzxcvbnm")
#         a3=random.choice("qwertyuiopasdfghjklzxcvbnm")
#         print(a1,a2,a3,a,b,c,sep="")
# taobiensoxe()
#bai96


# def ktra(p):
#     hoa=False
#     thuong=False
#     so=False
#     for bienktra in p:
#         if bienktra>="A" and bienktra<="Z":
#             hoa= True
#         if bienktra>="a" and bienktra<="z":
#             thuong=True
#         if bienktra>="0" and bienktra<="9":
#             so=True
#     if len(p)>=8 and hoa and thuong and so: return True
#     return False
# def main():
#     p=str(input("mật khẩu bạn tạo là: "))
#     if ktra(p):
#         print("mật khẩu tốt")
#     else:
#         print("mật khẩu không tốt")
# main()


