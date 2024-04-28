counter = 0
for i in range(11, 10000):
    num = i
    for j in range(50):
        num = num + int(str(num)[::-1])
        if str(num) == str(num)[::-1]:
            break
    else:
        counter += 1

print(counter)
