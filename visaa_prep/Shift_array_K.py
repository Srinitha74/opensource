A = int(input())
Array = list(map(int, input().split()))
K = int(input())
K = K % A
rotated_array =  Array[-K:] + Array[:-K]
print(" ".join(map(str,rotated_array)))
