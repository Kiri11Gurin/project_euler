import fractions
def rec(j):
    if j == len(period) - 1:
        return 1 / fractions.Fraction(period[j])
    else:
        return 1 / (period[j] + fractions.Fraction(rec(j + 1)))


max_x = 0
for num in range(2, 1001):
    if num ** 0.5 != int(num ** 0.5):
        ost = 0
        numer = 1
        denom = 1
        period = []
        while True:
            i = 1
            while (num ** 0.5 + ost) * numer - i * denom > 0:
                i += 1
            period.append(i - 1)
            ost = (i - 1) * (denom / numer) - ost
            numer = denom / numer
            denom = num - ost ** 2
            if len(period) <= 1:
                continue
            x = fractions.Fraction(period[0] + rec(1))
            if x.numerator ** 2 - num * x.denominator ** 2 == 1:
                print(f'd = {num}, {x}')
                if x.numerator > max_x:
                    max_x = x.numerator
                    max_d = num
                break

print(fr'd = {max_d}, x = {max_x}')
