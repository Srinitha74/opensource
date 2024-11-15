def ways(X):
    from math import factorial
    no_of_ways = factorial(X)
    return no_of_ways
X = int(input())
print(ways(X))
