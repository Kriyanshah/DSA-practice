t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())
    list = [a,b,c]
    list.sort()
    if list[2] == list[1] == 1:
        print("Not now")
    else:
        print("Water filling time")
    