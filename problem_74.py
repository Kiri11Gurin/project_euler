def digit_fact(n: int) -> int:
    """Функция считает сумму факториалов цифр числа."""
    total = 0
    factorials = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120,
                  '6': 720, '7': 5040, '8': 40320, '9': 362880}
    for i in str(n):
        total += factorials[i]
    return total

def euler_74(x: int) -> list:
    y = digit_fact(x)
    sp = [x]
    while y not in sp:
        sp.append(y)
        y = digit_fact(y)
    # return f'длина = {len(sp) - 1}', sp[:-1]
    return sp

counter = 0
for i in range(3, 10 ** 6 + 1):
    x = euler_74(i)
    if len(x) == 60:
        counter += 1
print(counter)  # 402
