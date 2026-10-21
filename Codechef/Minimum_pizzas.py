t = int(input())
for _ in range(t):
    n,x = map(int, input().split())
    d=n*x
    if d%4==0:
        print(d//4)
    else:
        print((d//4)+1)