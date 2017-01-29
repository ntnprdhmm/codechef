def calc_answ(n, a):
    c = 0
    # go throught array
    for i in range(n):
        # foreach subarray starting at index i, check if the sum and product are equals
        s = 0
        p = 1
        for j in range(i, n):
            s = s + a[j]
            p = p * a[j]

            if s == p:
                c = c + 1
    return c

for _ in range(int(input())):
    n = int(input())
    a = [int(v) for v in input().split()]
    print(calc_answ(n, a))