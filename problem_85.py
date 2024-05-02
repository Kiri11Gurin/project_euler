def euler_85():
    diff, closest, a, b = float('inf'), float('inf'), float('inf'), float('inf')
    for i in range(1, 2000):
        for j in range(1, i + 1):
            total = sum(range(1, i + 1)) * sum(range(1, j + 1))
            if abs(2e6 - total) < diff:
                diff = abs(2e6 - total)
                closest = total
                a, b = i, j
            if total >= 2e6:
                break
    print(f'{a = }, {b = }, {diff = }, {closest = }')
    print(f'area = {a * b}')
