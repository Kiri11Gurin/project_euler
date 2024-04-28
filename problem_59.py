import re
with open(r"p059_cipher.txt") as file:
    contents = list(map(int, file.read().split(',')))

sp_1 = []
sp_2 = []
sp_3 = []
for i in range(0, len(contents), 3):
    sp_1.append(contents[i])
    sp_2.append(contents[i + 1])
    sp_3.append(contents[i + 2])

sp_num_1 = []
sp_num_2 = []
sp_num_3 = []
for j in range(97, 123):
    new_sp_1 = list(map(lambda x: chr(j ^ x), sp_1))
    new_sp_2 = list(map(lambda x: chr(j ^ x), sp_2))
    new_sp_3 = list(map(lambda x: chr(j ^ x), sp_3))
    if all(map(str.isprintable, new_sp_1)):
        sp_num_1.append(j)
    if all(map(str.isprintable, new_sp_2)):
        sp_num_2.append(j)
    if all(map(str.isprintable, new_sp_3)):
        sp_num_3.append(j)
def fun():
    for i in sp_num_1:
        for j in sp_num_2:
            for k in sp_num_3:
                temp_text = ''
                for num in range(len(sp_1)):
                    temp_text += chr(sp_1[num] ^ i) + chr(sp_2[num] ^ j) + chr(sp_3[num] ^ k)
                match = re.fullmatch(r'[^$%@#~`]*', temp_text)
                if match:
                    return temp_text

print(sum(map(lambda x: ord(x), fun())))
