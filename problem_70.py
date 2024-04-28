import fractions
def euler(n):
    phi = 1
    for i in range(2, n):
        if fractions.Fraction(n, i).numerator == n:
            phi += 1
    return phi


def euler_prime(num_1, num_2):
    if num_1 == num_2:
        return num_1 * num_2 - num_1
    else:
        return num_1 * num_2 - (num_1 + num_2 - 1)


n = 10 ** 7 - 1
num_1 = 11111
# num_1 = 11
min_value = 10
while num_1 > 3:
    while not is_prime(num_1):
        num_1 -= 2
    num_2 = num_1
    if num_1 * num_2 < n:
        num_2 = num_1
    else:
        if int(n / num_1) % 2 == 1:
            num_2 = int(n / num_1)
        else:
            num_2 = int(n / num_1) + 1
    while num_2 > 3:
        if is_prime(num_2):
            if sorted(str(num_1 * num_2)) == sorted(str(euler_prime(num_1, num_2))):
                break
            else:
                num_2 -= 2
        else:
            num_2 -= 2
    if sorted(str(num_1 * num_2)) == sorted(str(euler_prime(num_1, num_2))):
        print(num_1, num_2, num_1 * num_2, num_1 * num_2 / euler_prime(num_1, num_2))
        if min_value > num_1 * num_2 / euler_prime(num_1, num_2):
            min_value = num_1 * num_2 / euler_prime(num_1, num_2)
            a, b = num_1, num_2
    num_1 -= 2
print()
print(a, b, a * b, min_value)
print(euler(a * b), euler_prime(a, b))
