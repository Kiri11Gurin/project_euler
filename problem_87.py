def is_prime(n: int) -> int:
    """Функция проверяет простое ли число."""
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True


def euler_87():
    upper_limit = 5e7
    prime_nums = [2]
    i = 3
    while i < upper_limit ** 0.5:
        if is_prime(i):
            prime_nums.append(i)
        i += 2
    print(prime_nums)
    nums = set()
    for i_4 in prime_nums:
        if 2 ** 2 + 2 ** 3 + i_4 ** 4 >= upper_limit:
            break
        for i_3 in prime_nums:
            if 2 ** 2 + i_3 ** 3 + i_4 ** 4 >= upper_limit:
                break
            for i_2 in prime_nums:
                if i_2 ** 2 + i_3 ** 3 + i_4 ** 4 < upper_limit:
                    nums.add(i_2 ** 2 + i_3 ** 3 + i_4 ** 4)
                else:
                    break
    return len(nums)


print(euler_87())
