num = int(input())
mirror_matrix= []
for _ in range(num):
    row = list(map(int,input().strip().split()))
    mirror_matrix = row[::-1]
    print(" ".join(map(str, mirror_matrix)))
