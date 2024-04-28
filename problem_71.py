import fractions
closest = fractions.Fraction(299999, 700000)
n = 299999
d = 700000
while d <= 10 ** 6:
    while (num := fractions.Fraction(n, d)) < fractions.Fraction(3, 7):
        if num > closest:
            closest = num
        n += 1
    d += 1
    n -= 1
print(closest)
