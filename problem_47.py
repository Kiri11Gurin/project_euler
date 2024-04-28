sp = [2]
for i in range(3, 1000000):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        sp.append(i)
counter = 0
limit = 4
for i in range(2, 1000000):
    if counter == limit:
        print(i - limit)
        break
    j = 0
    s = set()
    while i != 1:
        if i % sp[j] == 0:
            i /= sp[j]
            s.add(sp[j])
        else:
            j += 1
    else:
        if len(s) == limit:
            counter += 1
        else:
            counter = 0
            s = set()
