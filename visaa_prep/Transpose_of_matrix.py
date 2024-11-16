Num = int(input())
matrix = []
for _ in  range(Num):
    row = list(map(int,input().split()))
    matrix.append(row)
transpose = []
for col in range(Num):
    new_row = [matrix[row][col] for row in range(Num)]
    transpose.append(new_row)
for row in transpose:
    print(" ".join(map(str,row)))
