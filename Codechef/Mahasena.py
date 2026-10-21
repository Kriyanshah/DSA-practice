n = int(input())
a = list(map(int, input().split()))
b = 0
c = 0
for i in range(len(a)):
    if a[i] % 2 ==0:
        b+=1
    else:
        c+=1
if b>c:
    print("ready for battle")
else:
    print("not ready")