n = int(input())
total = n
for i in range(n-1, 1, -1):
    total = total * i
if total == 0:
    print(1)
else:
    print(total)