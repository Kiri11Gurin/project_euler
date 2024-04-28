with open(r"0081_matrix.txt") as file:
    contents = [list(map(int, i.strip().split(','))) for i in file.readlines()]

matrix = [[0] * 80 for i in range(80)]
matrix[0][0] = contents[0][0]
for i in range(1, 80):
    matrix[0][i] = contents[0][i] + matrix[0][i-1]
    matrix[i][0] = contents[i][0] + matrix[i-1][0]
for i in range(1, 80):
    for j in range(1, 80):
        matrix[i][j] = min((matrix[i-1][j], matrix[i][j-1])) + contents[i][j]
print(matrix[-1][-1])
