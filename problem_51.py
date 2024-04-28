import re
sp = []
for i in range(100001, 1000000, 2):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        sp.append(str(i))
def fun():
    for i in sp:
        res = re.fullmatch(r'\d*(\d)\d*(\1)\d*(\1)\d', i)
        if res:
            counter = 0
            for j in range(10):
                if i.replace(res.group(1), str(j), 3) in sp:
                    counter += 1
            if counter == 8:
                return i
print(fun())
