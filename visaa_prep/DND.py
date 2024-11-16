A, B = map(int,input().split())
Arr = map(int,input().split())
even_sum = 0
odd_sum = 0
for i in Arr:
    if i % B == 0 :
        even_sum -= i
    else:
        odd_sum -= i
print(odd_sum - even_sum)
    
