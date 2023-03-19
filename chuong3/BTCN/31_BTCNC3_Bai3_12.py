n=(input(''))
char='ABCDEFGHKL'
if int(n)>=0 and int(n)<=9999:
    i=0
    while i<len(n):
        print(char[int(n[i])],end='')
        i=i+1