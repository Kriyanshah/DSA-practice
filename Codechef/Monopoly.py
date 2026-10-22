t = int(input())
for _ in range(t):
    p,q,r,s = map(int, input().split())
    list = [p,q,r,s]
    list.sort()
    if list[3]> list[1]+list[2]+list[0]:
        print("yes")
    else:
        print("no")