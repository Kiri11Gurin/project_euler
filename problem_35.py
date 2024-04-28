import re
sp = []
for i in range(2, 10 ** 6):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        match = re.search(r'[02468]', str(i))
        if not match or i < 10:
            sp.append(i)
print(sp)
print(len(sp))
counter = 0
for i in sp:
    num = str(i)
    for j in range(len(str(i)) - 1):
        num = num[1:] + num[0]
        if int(num) not in sp:
            break
    else:
        counter += 1
print(counter)
