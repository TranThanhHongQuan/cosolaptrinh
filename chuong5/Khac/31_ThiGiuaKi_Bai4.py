n = int(input())
if n>0 and n<10**6:
    if n < 10:
        print("0")
    else:
        so1 = (n % 100) % 10
        so2 = (n % 100) // 10
        tong = so1 + so2
        print(tong)