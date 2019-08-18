count = 0
count1 = 0


def binomial(N, k, p):
    global count
    count += 1
    if N == 0 and k == 0:
        return 1.0
    if N < 0 or k < 0:
        return 0.0
    return (1.0 - p) * binomial(N - 1, k, p) + p * binomial(N - 1, k - 1, p)


def matrix_binomial(N, k, p, matrix):
    global count1
    count1 += 1
    if N == 0 and k == 0:
        return 1.0
    if N < 0 or k < 0:
        return 0.0
    if matrix[N][k] == -1.0:
        matrix[N][k] = (1.0 - p) * matrix_binomial(N - 1, k, p, matrix) + p * matrix_binomial(N - 1, k - 1, p,
                                                                                              matrix)
        # 用matrix保存已经计算过的值 不用重复计算
    return matrix[N][k]


def main():
    matrix = []
    N = 20
    k = 10
    p = 0.25

    for row in range(N + 1):
        matrix.append([-1.0] * (k + 1))
        # for column in range(k + 1):
        #     matrix[row].append(-1.0)

    print(binomial(N, k, p))
    print(count)
    print(matrix_binomial(N, k, p, matrix))
    print(count1)


if __name__ == '__main__':
    main()
