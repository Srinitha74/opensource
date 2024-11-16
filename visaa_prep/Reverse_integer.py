n = int(input())
n_min = -2**31
n_max =  2**31 - 1  
is_neg = n < 0
reverse=int(str(abs(n))[::-1]) 
if is_neg:
    reverse =- reverse
if reverse < n_min or reverse > n_max :
    print("0")
else:
    print(reverse)
