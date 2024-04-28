import fractions
import sys
sys.setrecursionlimit(1100)
def rec(n):
    if n == 1:
        return 1 / 2
    else:
        return 1 / (2 + fractions.Fraction(rec(n - 1)))
counter = 0

for i in range(1, 1001):
    num = fractions.Fraction(1 + rec(i))
    if len(str(num.numerator)) > len(str(num.denominator)):
        counter += 1

print(counter)
