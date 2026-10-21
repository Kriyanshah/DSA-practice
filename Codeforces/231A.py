n = int(input())
a = 0
for i in range(n):
    solve = list(map(int, input().split()))
    solve.sort()
    if solve[-1] == solve[-2] == 1:
        a += 1
print(a)
