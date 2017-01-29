for _ in range(int(input())):
    n, m = [int(v) for v in input().split()]
    a = input().split()
    b = input().split()
    counter = 0
    for c in a:
        if c in b:
            counter = counter + 1
    print(counter)