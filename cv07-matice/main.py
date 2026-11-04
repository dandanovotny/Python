from matrix import plus, zeros, minus, eyes, format, T, multiply, replace_row, replace_collum

if __name__ == "__main__":
    matrix_a = [
        [1, 0, 1],
        [0, 1, 0],
        [0, 0, 1]
    ]

    matrix_b = [
        [1, 1, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]

#matrix_c = plus(matrix_a, matrix_b)

# 2, 1, 2
# 1, 2, 1
# 1, 1, 2

#format(T(matrix_c))
#multiply(format(matrix_a, matrix_b))
format(replace_row(matrix_b, [5, 5, 5], 1))

print(eyes(4, 5))