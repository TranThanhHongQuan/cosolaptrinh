
kw=int(input("Tieu thu="))
if kw<=100:
    giatien=kw*550
elif kw<=150:
    giatien=100*550+(kw-100)*750
elif kw<=200:
    giatien=100*550+50*750+(kw-150)*950
elif 201<=kw:
    giatien=100*550+50*750+50*950+(kw-150)*1350
vat=giatien*(10/100)
print("Phai tra=",giatien+vat,sep="")