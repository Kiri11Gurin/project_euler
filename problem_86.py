import math
def mutually_prime(m, n):
    min_num = min(m, n)
    for i in range(2, min_num + 1):
        if m % i == 0 and n % i == 0:
            return False
    else:
        return True


counter = 0
M = 99
while counter <= 1e6:
    counter = 0
    M += 1
    for m in range(2, 80):
        for n in range(1, m):
            if (m - n) % 2 == 1 and mutually_prime(m, n):
                a = m ** 2 - n ** 2
                b = 2 * m * n
                k = 1
                while min(a * k, b * k) <= M:
                    max_num = max(a * k, b * k)
                    min_num = min(a * k, b * k)
                    if math.ceil(max_num / 2) > M:
                        break
                    # print(f'{m = }, {n = }, a = {a * k}, b = {b * k}:')
                    if max_num <= M:
                        temp_counter = min_num // 2
                        counter += temp_counter
                        # print(f'counter_min = {temp_counter}')
                    if max_num - 1 <= M and min_num >= max_num // 2:
                        temp_counter = min_num - math.ceil(max_num / 2) + 1
                        counter += temp_counter
                        # print(f'counter_max_1 = {temp_counter}')
                    elif M >= min_num >= max_num // 2:
                        temp_counter = min_num - math.ceil(max_num / 2) + 1
                        counter += temp_counter
                        # print(f'counter_max_2 = {temp_counter}')
                    k += 1
print(M)


# медленный способ:
# counter = 0
# for a in range(1, M + 1):
#     for b in range(a, M + 1):
#         for c in range(b, M + 1):
#             if ((a + b) ** 2 + c ** 2) ** 0.5 == int(((a + b) ** 2 + c ** 2) ** 0.5):
#                 print(f'{a = }, {b = }, {c = } | P = {a + b + c}')
#                 counter += 1
# print(f'{counter = }')
