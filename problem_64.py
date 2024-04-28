import re
max_len = 0
counter = 0
for num in range(2, 10001):
    if num ** 0.5 != int(num ** 0.5):
        ost = 0
        numer = 1
        denom = 1
        period = []
        for j in range(2000):
            i = 1
            while (num ** 0.5 + ost) * numer - i * denom > 0:
                i += 1
            period.append(i - 1)
            ost = (i - 1) * (denom / numer) - ost
            numer = denom / numer
            denom = num - ost ** 2
        else:
            s = '-'.join(str(e) for e in period)
            tire = 100
            while s[tire] != '-':
                tire += 1
            s = s[tire + 1:]
            r = re.search(r'((?:\d+-)+)(\1)(\1)(\1)', s)
            kol = 2
            while 1:
                for n in range(0, len(r.group(1)) - kol, kol):
                    if r.group(1)[n:n + kol] != r.group(1)[n + kol: n + 2 * kol]:
                        break
                else:
                    if max_len < len(r.group(1)[:kol]):
                        max_len = r.group(1)[:kol].count('-')
                        max_num = num
                    if r.group(1)[:kol].count('-') % 2 == 1:
                        counter += 1
                    break
                kol += 2
                while len(r.group(1)) % kol != 0 or r.group(1)[kol - 1] != '-':
                    kol += 1
print(counter, max_len, max_num)
