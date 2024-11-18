n=int(input())
arr=list(map(int,input().split()))
left_weight = 0
right_weight = 0
t_sum = sum(arr)
B = []
for i in range(n):
    right_weight = t_sum - left_weight - arr[i] 
    B.append(abs(left_weight - right_weight))
    left_weight += arr[i]
print(' '.join(map(str,B)))
            
            
