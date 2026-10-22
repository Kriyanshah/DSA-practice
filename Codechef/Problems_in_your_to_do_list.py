t = int(input())
for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    count=0
    for j in b:
        if j>=1000:
            count+=1
    print(count)    