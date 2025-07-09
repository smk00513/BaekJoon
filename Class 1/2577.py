a = int(input())
b = int(input())
c = int(input())
sum = a * b * c
s = list(map(int, str(sum)))
a = [0] * 10
for i in range(len(s)):
    a[s[i]] += 1
for _ in a:
    print(_)