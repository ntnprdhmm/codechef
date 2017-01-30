# for each test case 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    uncle_johny_length = a[k-1]
    a.sort()
    print(a.index(uncle_johny_length) + 1)