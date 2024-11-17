def position(arr, X, N) :
    l, r = 0, N - 1
    while l <= r :
        m = (l + r) // 2
        if arr[m] == X:
            return m
        elif arr[m] < X :
            l = m + 1
        else:
            r = m - 1
    return l
N, K = map(int,input().split())
arr = list(map(int,input().split()))
print(position(arr, K, N))
