X,Y,Z = map(int,input().split())
time_required = X * Y
available_time = Z * 24 * 60
if time_required <= available_time :
    print("YES")
else:
    print("NO")
        
