# for each test case
for _ in range(int(input())):
    n = int(input())
    s = [int(v) for v in input().split()]
    s.sort()
    # find the minimun diff
    min_diff = 10000000000000000000000
    for i in range(1, n):
        if s[i] - s[i-1] < min_diff:
            min_diff = s[i] - s[i-1]
    print(min_diff)
