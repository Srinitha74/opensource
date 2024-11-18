def m_avg_subarray(n, num_array, k):
    c_sum = sum(num_array[:k])
    m_sum = c_sum
    for i in range(k, n):
        c_sum += num_array[i] - num_array[i-k]
        m_sum = max(m_sum, c_sum)
    m_avg = m_sum / k
    return m_avg
n, k = map(int,input().split())
num_array = list(map(int,input().split()))
res = m_avg_subarray(n, num_array, k)
print(f"{res:.4f}")
