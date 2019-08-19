class Matrix:
    def dot(self, x, y):  # 向量相乘
        if len(x) != len(y):
            return 'error'
        res = 0
        for i in range(len(x)):
            res += x[i] * y[i]
        return res

    def transpose(self, a):  # 矩阵转制
        len_a = len(a)
        len_b = len(a[0])
        res = []
        for i in range(len_b):
            res.append([0] * len_a)
        for i in range(len_a):
            for j in range(len_b):
                res[j][i] = a[i][j]
        return res

    def mult_m_m(self, a, b):  # 矩阵乘法
        len_a = len(a)
        len_b = len(b[0])
        res = []
        for i in range(len_a):
            res.append([0] * len_b)
        for i in range(len_a):
            for j in range(len_b):
                for k in range(len(b)):
                    res[i][j] += a[i][k] * b[k][j]
        return res

    def mult_m_v(self, a, x):
        list_x = [x]
        return matrix.mult_m_m(a, list_x)

    def mult_v_m(self, y, a):
        list_y = [y]
        return matrix.mult_m_m(list_y, a)


x_t = [1, 3, -4]
y_t = [4, -2, -1]
a_t = [[1, 3, 2], [1, 0, 0], [1, 2, 2]]
b_t = [[0, 0, 2], [7, 5, 1], [2, 0, 1]]
a_t_1 = [[1, 0, 2], [-1, 3, 1]]
b_t_1 = [[3, 1], [2, 1], [1, 0]]

matrix = Matrix()
print(matrix.dot(x_t, y_t))
print(matrix.transpose(a_t))
print(matrix.mult_m_m(a_t_1, b_t_1))
print(matrix.mult_m_v(a_t, x_t))
print(matrix.mult_v_m(y_t, a_t))
