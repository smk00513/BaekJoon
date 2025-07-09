import math

def f(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    for i in num:
        if f(i):
            cnt += 1
    print(cnt)