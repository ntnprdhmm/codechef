for _ in range(int(input())):
    n = int(input())
    r = 0
    # xor on each integer from 1 to n
    for i in range(n):
        r = r ^ (i+1)
        t = input() # ignore this input
    print(r)
    