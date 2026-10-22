t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    if x>y:
        print("car")
    elif y>x:
        print("bike")
    else:
        print("same")