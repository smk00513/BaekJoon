import math

n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())
T_cnt = 0
for i in sizes:
    if i > 0:
        T_cnt += math.ceil(i / t)
print(T_cnt)
print(n // p, n % p)