X,Y,Z=map(int,input().split())
if Z<X:
    print("0")
elif Z<(X+Y):
    print("1")
else:
    print("2")
