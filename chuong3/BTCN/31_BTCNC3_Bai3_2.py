m1=int(input("M1="))
m2=int(input("M2="))
m3=int(input("M3="))
s=int(input("S="))
if s<100:
    phaitra=s*m1
elif 101<s<150:
    phaitra=100*m1+(s-100)*m2
elif s>151:
    phaitra=100*m1+50*m2+(s-150)*m3
print("Phai tra=",phaitra,sep="")