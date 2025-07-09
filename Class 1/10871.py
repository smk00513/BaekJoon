list = []
n, x = map(int, input().split())
for i in map(int, input().split()):
    if i < x:
        list.append(i)
print(*list)