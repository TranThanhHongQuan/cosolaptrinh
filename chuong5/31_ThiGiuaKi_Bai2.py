n = int(input())
dem = 0
if n>=0 and n<=10**6:
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            dem += 1
print(dem)