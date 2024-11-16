def max_consecutive_absent_days(absnt):
    max_absent=0
    current_absent=0
    for day in absnt:
        if day == 0:
            current_absent += 1
            max_absent = max(max_absent,current_absent)
        else:
            current_absent = 0
    return max_absent
Num = int(input())
absnt = list(map(int,input().split()))
print(max_consecutive_absent_days(absnt))
