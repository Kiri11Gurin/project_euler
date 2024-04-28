with open(r"0083_matrix.txt") as file:
    contents = [list(map(int, i.strip().split(','))) for i in file.readlines()]
start, end = 0, 80
contents = [contents[i][start:end] for i in range(start, end)]

# Вывод матрицы в удобном виде:
print(" " * 6, end='')
for i in range(len(contents)):
    print(f'№{i}{" " * (4 - len(str(i)))}', end='')
print()
for i in range(len(contents)):
    print(f'{(2 - len(str(i))) * " "}№{i}: ', end='')
    for j in range(len(contents)):
        print(f'{" " * (4 - len(str(contents[i][j])))}{contents[i][j]}', end='|')
    print()

result = [[float('inf')] * len(contents) for i in range(len(contents))]
result[0][0] = contents[0][0]
print(*result, sep='\n')

new_result = {}
for i in range(len(contents)):
    for j in range(len(contents)):
        new_result.update({(i, j): [result[i][j], False]})

def euler_83():
    while new_result[(len(contents) - 1, len(contents) - 1)][0] == float('inf'):
        min_elem = min(filter(lambda x: x[1][1] is False, new_result.items()), key=lambda x: x[1])
        x, y = min_elem[0][0], min_elem[0][1]
        for i in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= i[0] <= len(contents) - 1 and 0 <= i[1] <= len(contents) - 1 and new_result[(i[0], i[1])][0] > (r := new_result[(x, y)][0] + contents[i[0]][i[1]]):
                new_result[(i[0], i[1])][0] = r
        new_result[(x, y)][1] = True
    return new_result


print(euler_83())
