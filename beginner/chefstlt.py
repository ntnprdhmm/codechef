def str_diff(s1, s2):
    diff = 0
    q_mark = 0
    for i in range(len(s1)):
        # if q_mark, increment q_mark counter
        if s1[i] == '?' or s2[i] == '?':
            q_mark = q_mark + 1
        # else if the chars are differents, increment diff
        elif s1[i] != s2[i]:
            diff = diff + 1
    return str(diff) + ' ' + str(diff + q_mark)

# for each test case
for _ in range(int(input())):
    str1 = input()
    str2 = input()
    print(str_diff(str1, str2))