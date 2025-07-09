T = int(input())
for i in range(T):
    r, s = map(str, input().split())
    ss = list(map(str, s))
    for i in range(len(ss)):
        ss[i] = ss[i] * int(r)
    print(''.join(ss))