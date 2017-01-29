import math
for _ in range(int(input())):
    b, ls = [int(v) for v in input().split()]
    max_v = math.sqrt(b*b + ls*ls)
    min_v = math.sqrt(ls*ls - b*b)
    print(str(min_v) + ' ' + str(max_v))