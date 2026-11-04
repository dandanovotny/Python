from matrix import plus, zeros, minus, eyes, format, T, multiply, replace_row, replace_collum, determinant, convolution
from view import load, numpy_to_list, list_to_numpy, show

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

    matrix_x = [
        [1, 1],
        [0, 1]
    ]

    kernel_1 = [
        [1, 0, -1],
        [1, 0, -1],
        [1, 0, -1]
    ]

    kernel_2 = [
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1]
    ]

    bluer_kernel = [
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
    ]

    emboss_kernel = [
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ]

    lapacian_kernel = [
        [0, 0, -1, 0, 0],
        [0, -1, -2, -1, 0],
        [-1, -2, 12, -2, -1],
        [0, -1, -2, -1, 0],
        [0, 0, -1, 0, 0]
    ]

    gaussian_kernel = [
        [1, 4, 6, 4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1, 4, 6, 4, 1]
    ]


#matrix_c = plus(matrix_a, matrix_b)

# 2, 1, 2
# 1, 2, 1
# 1, 1, 2

#format(T(matrix_c))
#multiply(format(matrix_a, matrix_b))
format(replace_row(matrix_b, [5, 5, 5], 1))
print(determinant(matrix_x))
print(eyes(4, 5))

image = load("C:\\Users\\daniel.novotny\\Desktop\\Flowers.webp")

img = numpy_to_list(image)
#new_img = convolution(img, kernel_1)
#new_img_2 = convolution(img, kernel_2)
#new_img_3 = convolution(img, kernel_1)
#result = plus(new_img, new_img_2)
result = convolution(img, lapacian_kernel)
np_img = list_to_numpy(result)
show(np_img)