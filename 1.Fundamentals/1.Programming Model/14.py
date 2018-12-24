import copy
matrix = [[1,2,3],[4,5,6],[7,8,9]]

temp_matrix = copy.deepcopy(matrix)

for y in range(len(matrix)):
    for x in range(len(matrix)):
        matrix[y][x] = temp_matrix[x][y]
print(matrix)
