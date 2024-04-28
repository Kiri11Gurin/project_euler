with open(r"0082_matrix.txt") as file:
    contents = [list(map(int, i.strip().split(','))) for i in file.readlines()]
contents = list(zip(*contents))
matrix = [[0] * len(contents) for i in range(len(contents))]
for i in range(len(contents)):
    matrix[0][i] = contents[0][i]
for i in range(1, len(contents)):
    for j in range(len(contents)):
        min_sum = matrix[i-1][j] + contents[i][j]
        for k in range(len(contents)):
            l_bound = min((j, k))
            u_bound = max((j, k)) + 1
            if (value := matrix[i-1][k] + sum(contents[i][l_bound:u_bound])) < min_sum:
                min_sum = value
        matrix[i][j] = min_sum
print(min(matrix[-1]))
