# for each test case
for _ in range(int(input())):
    tra_ign = 0     # tracked + ignored
    unt_uni = 0     # untracker + unignored
    # N : nb files / M : nb ignored / K : nb tracked
    n, m, k = [int(v) for v in input().split()]
    # A : the M ignored source files
    a = [int(v) for v in input().split()]
    # B : the K tracked source files
    b = [int(v) for v in input().split()]
    # for throught files
    for i in range(1, n+1):
        if i in a:
            if i in b:
                tra_ign = tra_ign + 1
        else:
            if i not in b:
                unt_uni = unt_uni + 1
    print(str(tra_ign) + ' ' + str(unt_uni))