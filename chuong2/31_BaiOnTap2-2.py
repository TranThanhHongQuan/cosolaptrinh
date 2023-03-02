gianiemyet = int(input("nhap gia niem yet: "))
Chietkhau = int(input("nhap gia chiet khau: "))
VAT = (gianiemyet - Chietkhau) * 0.01
Giaban = gianiemyet - Chietkhau + VAT
print("Gia ban:",Giaban)
