A = int(input())
Array = list(map(int,input().split()))
unique_elements = []
s = set()
for n in Array:
    if n not in s :
        unique_elements.append(n)
        s.add(n)
print(" ".join(map(str,unique_elements)))
