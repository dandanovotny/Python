from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def load(cesta):
    img = Image.open(cesta).convert("L")
    matrix = np.array(img)
    return matrix

def show(matrix):
    plt.imshow(matrix, cmap="gray")
    plt.colorbar()
    plt.show()

matrix = load("C:\\Users\\daniel.novotny\\Desktop\\Flowers.webp")
show(matrix)