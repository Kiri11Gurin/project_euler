primes = []
for i in range(3, 10000, 2):
    if is_prime(i) and i != 5:
        primes.append(i)

for i_1 in range(len(primes) - 4):
    for i_2 in range(i_1 + 1, len(primes)):
        if is_prime(int(str(primes[i_1]) + str(primes[i_2]))) and is_prime(
                int(str(primes[i_2]) + str(primes[i_1]))):
            for i_3 in range(i_2 + 1, len(primes)):
                if is_prime(int(str(primes[i_1]) + str(primes[i_3]))) and is_prime(
                        int(str(primes[i_3]) + str(primes[i_1]))) and is_prime(
                    int(str(primes[i_2]) + str(primes[i_3]))) and is_prime(
                    int(str(primes[i_3]) + str(primes[i_2]))):
                    for i_4 in range(i_3 + 1, len(primes)):
                        if is_prime(int(str(primes[i_1]) + str(primes[i_4]))) and is_prime(
                                int(str(primes[i_4]) + str(primes[i_1]))) and is_prime(
                            int(str(primes[i_2]) + str(primes[i_4]))) and is_prime(
                            int(str(primes[i_4]) + str(primes[i_2])))and is_prime(
                            int(str(primes[i_3]) + str(primes[i_4]))) and is_prime(
                            int(str(primes[i_4]) + str(primes[i_3]))):
                                for i_5 in range(i_4 + 1, len(primes)):
                                    if is_prime(int(str(primes[i_1]) + str(primes[i_5]))) and is_prime(
                                            int(str(primes[i_5]) + str(primes[i_1]))) and is_prime(
                                        int(str(primes[i_2]) + str(primes[i_5]))) and is_prime(
                                        int(str(primes[i_5]) + str(primes[i_2]))) and is_prime(
                                        int(str(primes[i_3]) + str(primes[i_5]))) and is_prime(
                                        int(str(primes[i_5]) + str(primes[i_3]))) and is_prime(
                                        int(str(primes[i_4]) + str(primes[i_5]))) and is_prime(
                                        int(str(primes[i_5]) + str(primes[i_4]))):
                                            print(primes[i_1], primes[i_2], primes[i_3], primes[i_4], primes[i_5], 'сумма =',
                                                  sum([primes[i_1], primes[i_2], primes[i_3], primes[i_4], primes[i_5]]))
