def find_altitude(n, heights):
    alt = 0
    max_alt = alt
    for h in heights:
        alt += h
        max_alt = max(max_alt, alt)
    return max_alt
n =  int(input())
arr = list(map(int,input().split()))
print(find_altitude(n,arr))
