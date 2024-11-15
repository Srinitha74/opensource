A = int(input())
array = list(map(int,input().split()))
rotated_array = array[1:] + array[:1]
print(' '.join(map(str, rotated_array)))
