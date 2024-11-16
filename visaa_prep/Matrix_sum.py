number = int(input())
matrix = []
for _ in range(number):
    row = list(map(int, input().split()))
    matrix.append(row)
sum_of_row = [0] * number
sum_of_col = [0] * number
for i in range(number):
    for j in range(number):
        sum_of_row[i] += matrix[i][j]
        sum_of_col[j] += matrix[i][j]
A = [0] * number
for i in range(number):
    A[i] = sum_of_row[i] + sum_of_col[i]
print(" ".join(map(str,A)))
