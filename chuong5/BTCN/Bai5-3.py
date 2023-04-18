n=int(input("n="))
L=[]
dem=0
tong=0
songuyenchan=0
TBC=0
for i in range (1,n+1):
    x=int(input())
    L=L+[x]
    if x > 0 :
        dem=dem+1
    if x % 2==0:
        tong=tong+x
        songuyenchan+=1
        TBC=tong/songuyenchan
print("SND=",dem,sep="")
print("TBC=",TBC,sep="")


    

