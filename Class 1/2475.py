def f(a):
    result = 0
    for i in range(len(a)):
        result += a[i] * a[i]
    return result

if __name__ == '__main__':
    a = list(map(int, input().split()))
    print(f(a) % 10)