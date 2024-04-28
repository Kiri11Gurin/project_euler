import itertools
# 3
n = 1
num_3 = n * (n + 1) // 2
num_3_sp = []
while num_3 < 10000:
    if num_3 >= 1010 and str(num_3)[2] != '0':
        num_3_sp.append(num_3)
    n += 1
    num_3 = n * (n + 1) // 2
num_3_str = ' ' + ' '.join(str(e) for e in num_3_sp) + ' '
# 4
n = 1
num_4 = n ** 2
num_4_sp = []
while num_4 < 10000:
    if num_4 >= 1010 and str(num_4)[2] != '0':
        num_4_sp.append(num_4)
    n += 1
    num_4 = n ** 2
num_4_str = ' ' + ' '.join(str(e) for e in num_4_sp) + ' '
# 5
n = 1
num_5 = n * (3 * n - 1) // 2
num_5_sp = []
while num_5 < 10000:
    if num_5 >= 1010 and str(num_5)[2] != '0':
        num_5_sp.append(num_5)
    n += 1
    num_5 = n * (3 * n - 1) // 2
num_5_str = ' ' + ' '.join(str(e) for e in num_5_sp) + ' '
# 6
n = 1
num_6 = n * (2 * n - 1)
num_6_sp = []
while num_6 < 10000:
    if num_6 >= 1010 and str(num_6)[2] != '0':
        num_6_sp.append(num_6)
    n += 1
    num_6 = n * (2 * n - 1)
num_6_str = ' ' + ' '.join(str(e) for e in num_6_sp) + ' '
# 7
n = 1
num_7 = n * (5 * n - 3) // 2
num_7_sp = []
while num_7 < 10000:
    if num_7 >= 1010 and str(num_7)[2] != '0':
        num_7_sp.append(num_7)
    n += 1
    num_7 = n * (5 * n - 3) // 2
num_7_str = ' ' + ' '.join(str(e) for e in num_7_sp) + ' '
# 8
n = 1
num_8 = n * (3 * n - 2)
num_8_sp = []
while num_8 < 10000:
    if num_8 >= 1010 and str(num_8)[2] != '0':
        num_8_sp.append(num_8)
    n += 1
    num_8 = n * (3 * n - 2)
num_8_str = ' ' + ' '.join(str(e) for e in num_8_sp) + ' '
# all
all_sp = sorted(set(num_3_sp + num_4_sp + num_5_sp + num_6_sp + num_7_sp + num_8_sp))
all_str = ' ' + ' '.join(str(e) for e in all_sp) + ' '


def fun():
    d = {'3': num_3_sp, '4': num_4_sp, '5': num_5_sp, '6': num_6_sp, '7': num_7_sp, '8': num_8_sp}
    sp_prob = list(map(lambda x: ''.join(x), itertools.permutations('345678')))
    for var in sp_prob:
        for i_3 in d[var[0]]:
            for i_4 in d[var[1]]:
                if str(i_3)[2:] == str(i_4)[:2] and i_3 != i_4:
                    for i_5 in d[var[2]]:
                        if str(i_4)[2:] == str(i_5)[:2] and i_3 != i_5 and i_4 != i_5:
                            for i_6 in d[var[3]]:
                                if str(i_5)[2:] == str(i_6)[:2] and i_3 != i_6 and i_4 != i_6 and i_5 != i_6:
                                    for i_7 in d[var[4]]:
                                        if str(i_6)[2:] == str(i_7)[:2] and i_3 != i_7 and i_4 != i_7 and i_5 != i_7 and i_6 != i_7:
                                            for i_8 in d[var[5]]:
                                                if str(i_7)[2:] == str(i_8)[:2] and str(i_8)[2:] == str(i_3)[:2] and i_3 != i_8 and i_4 != i_8 and i_5 != i_8 and i_6 != i_8 and i_7 != i_8:
                                                    return i_3, i_4, i_5, i_6, i_7, i_8, sum([i_3, i_4, i_5, i_6, i_7, i_8])


print(fun())
