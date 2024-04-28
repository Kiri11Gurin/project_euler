def fun(den):
    x = ''
    num = 10
    while len(x) < 10000:
        while den > num:
            num *= 10
            x += '0'
        x += str(num // den)
        num = num % den * 10
        if num == 0:
            return x
    return x


max_chunk_len = 1
num_chunk = 0
for i in range(101, 1000):
    num = fun(i)
    chunk_len = 1
    while 1:
        if len(num) == 1:
            break
        elif num.find(num[0:chunk_len], chunk_len) == -1:
            num = num[1:]
            chunk_len = 1
        elif num.find(num[0:chunk_len], chunk_len) - chunk_len == 0:
            if num.find(num[0:chunk_len], 2 * chunk_len) - 2 * chunk_len == 0:
                # print('Число =', i,'Длина =', chunk_len)
                if max_chunk_len < chunk_len:
                    max_chunk_len = chunk_len
                    max_chunk = i
                break
            else:
                chunk_len += 1
        else:
            chunk_len = num.find(num[0:chunk_len], chunk_len)

print('Число =', max_chunk, 'Длина =', max_chunk_len)
