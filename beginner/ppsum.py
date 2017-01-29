# sum of the integers from 1 to N 
def sum(n):
    r = 0
    for i in range(1, n+1):
        r = r + i
    return r

# D times the sum of integers from 1 to N
def d_sum(d, n):
    if d > 0:
        return d_sum(d - 1, sum(n))
    else:
        return n

for _ in range(int(input())):
    d, n = [int(v) for v in input().split()]
    print(d_sum(d, n))