T=int(input())
for _ in range(0,T):
    N,M = map(int,input().split())
    if N>M:
        print(N-M)
    else:
        print("0")
