import sys

n, k = map(int, sys.stdin.readline().split())
c = 0
for _ in range(n):
    if int(sys.stdin.readline()) % k == 0:
        c = c + 1
print(c)