A = int(input())
if 1500 < A < 3000 :
    if A % 400 == 0:
        print("YES")
    elif A % 4 == 0 and A % 100 != 0 :
        print("YES")
    else:
        print("NO")
