letters = input().split()
for _ in range(int(input())):
    valid = True
    for c in input():
        if c not in letters:
            valid = False
            break
    print("Yes" if valid else "No")