import math
for _ in range(int(input())):
    n = int(input())
    print(int((math.pow(n//2, 2) - n//2) / 2))