n =  int(input())
for i in range(n):
    word = list((input().split()))
    for j in range(len(word)):
        a = word[j]
        if len(a) > 10:
            print(a[0] + str(len(a) - 2) + a[-1])
        else:
            print(a)