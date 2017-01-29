def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

# for each test case, display his factorial
for _ in range(int(input())):
    print(factorial(int(input())))