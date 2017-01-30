a, b = map(int, input().split())

r = a - b
if r % 10 == 9:
    print(r-1)
else:
    print(r+1)