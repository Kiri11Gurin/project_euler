sp = [99, 1]
number = sum(sp)
print(f'{number = }')
counter = 1
while sp[0] != 1:
    while sp[0] - 1 >= sp[1] + 1:
        sp[0] -= 1
        sp[1] += 1
        counter += 1
    else:
        for i in range(1, len(sp) - 1):
            if sp[i] >= sp[i + 1] + 1 and (sp[i + 1] + 1) * len(sp[:i + 2]) + sum(sp[i + 2:]) <= number:
                sp[i + 1] += 1
                sp[1:i + 1] = [sp[i + 1] for j in range(len(sp[1:i + 1]))]
                sp[0] = number - sum(sp[1:])
                counter += 1
                break
        else:
            sp = [1 for i in range(len(sp) + 1)]
            sp[0] = number - sum(sp[1:])
            counter += 1

print(f'{counter = }')
