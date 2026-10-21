t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    d = x*y
    print(d//100)