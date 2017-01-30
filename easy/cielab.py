a, b = map(int, input().split())

r = a - b
splitted_r = [int(i) for i in str(r)]

for idx in range(len(splitted_r)):
    if splitted_r[idx] > 1:
        splitted_r[idx] = splitted_r[idx] - 1
        break
    elif splitted_r[idx] < 9:
        splitted_r[idx] = splitted_r[idx] + 1
        break

print(''.join(str(i) for i in splitted_r))