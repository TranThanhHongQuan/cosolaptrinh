# #cau a
# def nhap():
#     so= []
#     for i in range (10):
#         nhapso=int(input())
#         so.append(nhapso)
#     songuyen=int(input("X="))
#     return so, songuyen
# def ktra(so,songuyen):
#     i=0
#     while i<(len(so)):
#         if so[i] == songuyen :
#             del(so[i]) 
#         i+=1 
# so,songuyen=nhap()
# ktra(so,songuyen)
# print(so)

#caub
def nhapvaluu():
    so= []
    for i in range (10):
        nhapso=int(input())
        so.append(nhapso)
    songuyen=int(input("X="))
    return so,songuyen
def timvathaycaua(so,songuyen):
    for i in range(len(so)):
        if so[i] == 5:
            so[i] = songuyen
def ktracaub(so,songuyen):
    i=0
    while i<(len(so)):
        if so[i] == songuyen :
            del(so[i])
        else: 
            i+=1 
so,songuyen=nhapvaluu()
timvathaycaua(so,songuyen)
print(so)
ktracaub(so,songuyen)
print(so)        





# mypet=["Cò","Hổ","Báo","Chồn"]
# print("Nhập Tên Thú cưng của you")
# name=input()
# if name not in mypet :
#     # mypet.append(name)
#     mypet=mypet+[name]
#     print(mypet)
# else:
#     print(name+" là thú cưng của tôi")