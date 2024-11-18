def find(N,array):
    for i in range(1,N):
        if array[i] < array[i-1]:
            return "false"
    return "true"
N = int(input())
array = list(map(int,input().split()))
print(find(N,array))
