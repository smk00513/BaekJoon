list = [0] * 30
for i in range(0, 28):
    a = int(input())
    list[a-1] = 1
for i in range(0, 30):
    if list[i] == 0:
        print(i+1)