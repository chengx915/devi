# 列表推导式中的初始表达式可以是任何表达式，甚至可以是另一个列表推导式
# 初始化一个矩阵
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# 转置matrix
anmatrix = [[row[i] for row in matrix] for i in range(4)]
anmatrix
# anmatrix = [
#   [1, 5, 9]
#   [2, 6, 10]
#   [3, 7, 11]
#   [4, 8, 12]
# ]


# matrix与anmatrix相乘

def multmatrix(a, b,):
    c = [[q[p] for q in a] for p in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            c[i][j] = 0
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]
    return c


print(multmatrix(matrix, anmatrix))
