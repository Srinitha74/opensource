def print_the_diamond_pattern(n):
    for i in range(1,n+1):
        print('*' *i, end='')
        print(' ' * (2*(n-i)),end='')
        print('*' *i)
    for i in range(n-1,0,-1):
        print('*' *i, end='')
        print(' ' * (2*(n-i)),end='')
        print('*' * i)
n = int(input())
print_the_diamond_pattern(n)
