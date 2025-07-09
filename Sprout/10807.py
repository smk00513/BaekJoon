n = int(input())
a = list(map(int, input().split()))
x = int(input())
cnt = 0
for _ in a:
    if _ == x:
        cnt += 1
print(cnt)