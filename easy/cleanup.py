# for each test case
for _ in range(int(input())):
    n, m = map(int, input().split())
    done = list(map(int, input().split()))
    chef = []
    assistant = []

    chef_turn = True

    for i in range(1, n+1):
        if i not in done:
            if chef_turn:
                chef.append(i)
            else:
                assistant.append(i)
            chef_turn = not chef_turn

    print(' '.join(str(i) for i in chef))
    print(' '.join(str(i) for i in assistant))