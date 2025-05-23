def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

N = int(input())

for _ in range(N):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m - n))
    print(bridge)