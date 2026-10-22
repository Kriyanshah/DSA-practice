t = int(input())
for _ in range(t):
    a,b,x,y = map(int, input().split())
    if x*y>=a*b:
        print("yes")
    else:
        print("no")