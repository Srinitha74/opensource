def perimeter(N,lengths):
    lengths.sort()
    for i in range(N-1,1,-1):
        if lengths[i-2]+lengths[i-1]>lengths[i]:
            return lengths[i-2]+lengths[i-1]+lengths[i]
    return -1
N=int(input())
lengths=list(map(int,input().split()))
res=perimeter(N,lengths)
print(res)
