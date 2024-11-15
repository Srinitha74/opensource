import math
a, b = map(int,input().split())
total_planes_required = math.ceil(b / 100)
new_planes_required = max(0, total_planes_required - a)
print(new_planes_required)
