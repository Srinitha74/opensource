def fix_the_grid(A, B, grid):
    r = set()
    c = set()
    for i in range(A):
        for j in range(B):
            if grid[i][j] == 0:
                r.add(i)
                c.add(j)
    for k in range(A):
        for l in range(B):
            if k in r or l in c:
                grid[k][l] = 0
    return grid
A, B = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(A)]
f_grid = fix_the_grid(A, B, grid)
for r in f_grid:
    print(' '.join(map(str, r)))
