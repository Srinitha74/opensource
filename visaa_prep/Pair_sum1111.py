def find_the_pair(array, K):
    seen = set()
    for num in array :
        c = K - num
        if c in seen :
            return True
        seen.add(num)
    return False
N = int(input())
elements = list(map(int,input().split()))
K = int(input())
if find_the_pair(elements, K):
    print("true")
else:
    print("false")
    
