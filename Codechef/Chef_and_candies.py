# cook your dish here
t = int(input())
for _ in range(t):
    n,x = map(int, input().split())
    if n>x:
        a = n-x 
        if a%4 == 0:
            print(a//4)
        else:
            print((a//4)+1)
    
    else:
        print(0)
        