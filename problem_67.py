sp_sum = [59 + 73, 59 + 41]
with open(r"p067_triangle.txt") as file:
    contents = list(map(int, file.read().split()))

new_contents = []
i = 1
while contents:
    new_contents.append(contents[0:i])
    del contents[0:i]
    i += 1

for i in range(2, len(new_contents)):
    sp_temp = sp_sum.copy()
    for j in range(1, len(new_contents[i]) - 1):
        sp_temp[j] = max((sp_sum[j - 1], sp_sum[j])) + new_contents[i][j]
    sp_temp[0] = sp_sum[0] + new_contents[i][0]
    sp_temp.append(sp_sum[-1] + new_contents[i][-1])
    sp_sum = sp_temp.copy()

print(max(sp_sum))
