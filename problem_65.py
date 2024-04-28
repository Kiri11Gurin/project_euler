import fractions
sp = [2]
i = 1
while len(sp) < 100:
    sp.extend([1, i * 2, 1])
    i += 1

def rec(j):
    if j == 99:
        return 1 / sp[j]
    else:
        return 1 / (sp[j] + fractions.Fraction(rec(j + 1)))


x = 2 + rec(1)
print(sum(map(int, str(x.numerator))))
