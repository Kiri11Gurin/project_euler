total_i, total_j = 1, 1
for i in range(11, 99):
    for j in range(i + 1, 100):
        if i % 10 != 0 and j % 10 != 0 and (set(str(i)) & set(str(j))):
            mutual_num = list(set(str(i)) & set(str(j)))[0]
            #print(i, j)
            if int(str(i).replace(mutual_num, "", 1)) / int(str(j).replace(mutual_num, "", 1)) == i / j:
                total_i *= i
                total_j *= j
                print(i, j)

import fractions
print(total_i, total_j)
print(fractions.Fraction(total_i, total_j))
