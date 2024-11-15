N = int(input())
if N >= 3 and N <= 5:
    print("Spring")
elif N >= 6 and N <= 8:
    print("Summer")
elif N >= 9 and N <= 11:
    print("Autumn")
elif N == 12 or N == 1 or N == 2 :
    print("Winter")
else:
    print("Invalid")
