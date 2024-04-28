counter = 0
num = 345
while counter != 5:
    counter = 0
    max_num = ''.join(sorted(str(num ** 3), reverse=True))
    num_2 = num
    while int(max_num) >= num_2 ** 3:
        if sorted(str(num_2 ** 3)) == sorted(max_num):
            counter += 1
        num_2 += 1
    num += 1
print((num - 1) ** 3)
