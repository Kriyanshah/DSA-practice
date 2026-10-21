t = int(input())
for i in range(t):
    x,y,z = map(int, input().split())
    if x*y//2 < z:
        print("yes")
    else:
        print("no")