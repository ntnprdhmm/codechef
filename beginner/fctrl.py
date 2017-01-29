# find the number of trailing zeros of the factorial of each number
for _ in range(int(input())):
    # use the "divide by 5" tip
    n = int(input())
    f = n // 5
    nb_0 = f
    while f >= 5:
        f = f // 5
        nb_0 = nb_0 + f
    print(nb_0)