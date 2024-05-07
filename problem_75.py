def mutually_prime(m, n):
    min_num = min(m, n)
    for i in range(2, min_num + 1):
        if m % i == 0 and n % i == 0:
            return False
    else:
        return True


counter = 0
d = {}
for m in range(2, 870):  # 870
    for n in range(1, m):
        if (m - n) % 2 == 1 and mutually_prime(m, n):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            k = 1
            while (a + b + c) * k <= 1500000:
                # print(f'a = {a * k}, a = {b * k}, a = {c * k}, P = {(a + b + c) * k}')
                d[(a + b + c) * k] = d.get((a + b + c) * k, 0) + 1
                k += 1
            k = 1

print(len(list(filter(lambda x: x[1] == 1, d.items()))))
