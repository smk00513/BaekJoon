t = int(input())
for _ in range(t):
    a = list(input())
    cnt = 0
    sum = 0
    for i in range(len(a)):
        if a[i] == 'O' or a[i] == 'o':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)