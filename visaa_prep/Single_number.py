def find(array):
    result = 0
    for i in array:
        if (3 <= i <= 1000):
            result ^= i
    return result
N = int(input())
array = list(map(int,input().split()))
print(find(array))
