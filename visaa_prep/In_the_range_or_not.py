def is_audible(f):
    return 67 <= f <= 45000
test_cases = int(input())
result = []
for _ in range(test_cases) :
    A = int(input())
    if is_audible(A):
        result.append("YES")
    else:
        result.append("NO")
for res in result :
    print(res)
