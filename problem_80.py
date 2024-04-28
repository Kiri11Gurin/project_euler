def euler_80(num):
    if len(str(num)) % 2 == 0:
        num = str(num)
    else:
        num = f'0{str(num)}'
    res = ''
    pair = int(num[0:2])
    sub = int(pair ** 0.5)
    res += str(sub)
    r = pair - sub ** 2
    for i in range(2, len(num), 2):
        pair = int(str(r) + num[i:i+2])
        j = 1
        while int(f'{str(int(res) * 2)}{j}') * j <= pair:
            j += 1
        r = pair - int(f'{str(int(res) * 2)}{j - 1}') * (j - 1)
        res += str(j - 1)

    while len(res) < 100:
        pair = int(str(r) + '00')
        j = 1
        while int(f'{str(int(res) * 2)}{j}') * j <= pair:
            j += 1
        r = pair - int(f'{str(int(res) * 2)}{j - 1}') * (j - 1)
        res += str(j - 1)
    return sum(map(int, res))

counter = 0
for i in range(2, 100):
    if int(i ** 0.5) != i ** 0.5:
        counter += euler_80(i)
print(counter)
