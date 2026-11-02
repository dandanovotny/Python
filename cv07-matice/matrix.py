def zeros(m, n):
    """
    Function creates empty matrix
    """
    matrix_c = []
    for i in range(m):
        matrix_c.append([])
        for j in range(n):
            matrix_c[i].append(0)
    return matrix_c

def plus(matrix_a, matrix_b):
    matrix_c = zeros(len(matrix_a), len(matrix_a[0]))
    for i in range(len(matrix_c)):
        for j in range(len(matrix_c[i])):
            matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return matrix_c

def minus(matrix_a, matrix_b):
    matrix_c = zeros(len(matrix_a), len(matrix_a[0]))
    for i in range(len(matrix_c)):
        for j in range(len(matrix_c[i])):
            matrix_c[i][j] = matrix_a[i][j] - matrix_b[i][j]
    return matrix_c

def eyes(m, n):
    """
    Vygeneruje jednotkovou matici
    """
    matrix = zeros(m, n)
    for i in range(m):
        for j in range(n):
            matrix[i].append(0)
            if i == j:
                matrix[i][j] = 1
    return matrix