N = int(input())
if 1 <= N <= 15:
    f = 1
    for i in range(1, N+1):
        f *= i
    print(f)
