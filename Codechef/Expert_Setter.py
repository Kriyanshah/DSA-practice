t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    if (y/x)*100 >= 50:
        print("yes")
    else:
        print("no")