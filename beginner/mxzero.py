for _ in range(int(input())):
    n = int(input())
    numbers = input()
    nb_1 = numbers.count('1')
    if nb_1 % 2 == 0:
        print(n - nb_1)
    else:
        print(nb_1)