max_sum = 0
for a in range(2, 101):
    if a % 10 != 0:
        for b in range(2, 101):
            if sum(map(int, str(a ** b))) > max_sum:
                max_sum = sum(map(int, str(a ** b)))
print(max_sum)
