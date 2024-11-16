Num =int(input())
K = int(input())
if Num & (1<<(K-1)) != 0:
    print("true")
else:
    print("false")
