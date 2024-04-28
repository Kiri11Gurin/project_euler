counter = 0
for num in range(2, 10 ** 6 + 1):
    d = {}
    pr = 1
    if num % (2 * 10 ** 5) == 0:
        print(num)
    temp_num = num
    divisor = 2
    while temp_num != 1:
        if divisor > num ** 0.5:
            divisor = temp_num
        if temp_num % divisor == 0:
            d[divisor] = d.get(divisor, 0) + 1
            temp_num //= divisor
        else:
            divisor += 1
    for k, v in d.items():
        pr *= k ** v - k ** (v - 1)
    counter += pr
print(counter)
