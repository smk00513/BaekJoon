def f(a, b):
    return (a + b) * (a - b)

if __name__ == '__main__':
    a, b  = map(int, input().split())
    print(f(a, b))