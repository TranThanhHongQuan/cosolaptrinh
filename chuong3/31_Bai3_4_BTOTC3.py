while True:
    a=int(input("a="))
    b=int(input("b="))
    c=(input("Toan tu:"))

    if c=="+":
        print(a,"+",b,"=",a+b)
        d=str(input("Tiep tuc:"))
    elif c=="-":
        print(a,"-",b,"=",a-b)
        d=str(input("Tiep tuc:"))
    elif c=="/":
        print(a,"/",b,"=",a/b)
        d=str(input("Tiep tuc:"))
    elif c=="*":
        print(a,"*",b,"=",a*b)
        d=str(input("Tiep tuc:"))
    if  d=="t" or d=="T" :
        break
    else:
        continue