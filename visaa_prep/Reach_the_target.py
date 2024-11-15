no_of_test_cases = int(input())
for _ in range(no_of_test_cases):
    Target, Current_Score = map(int,input().split())
    Runs_required = Target - Current_Score + 1
    print(Runs_required)
