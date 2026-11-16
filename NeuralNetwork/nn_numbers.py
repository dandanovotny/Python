
from matrix import *
from matrix import gen_random_matrix
import math
from tqdm import tqdm
import random
import os
import json
from PIL import Image


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_derivative_matrix(A):
    return apply(
        A,
        lambda x: x * (1 - x)
    )


def forward(X, W1, B1, W2, B2):

    Z1 = plus(multiply(W1, X), B1)
    A1 = apply(Z1, sigmoid)

    Z2 = plus(multiply(W2, A1), B2)
    A2 = apply(Z2, sigmoid)

    return Z1, A1, Z2, A2


def backward(X, Y, A1, A2, W1, B1, W2, B2, learning_rate):

    # Výstupní vrstva
    dZ2 = multiply_elementwise(
        minus(A2, Y),
        sigmoid_derivative_matrix(A2)
    )

    dW2 = multiply(dZ2, T(A1))
    dB2 = dZ2

    # Skrytá vrstva
    dA1 = multiply(T(W2), dZ2)

    dZ1 = multiply_elementwise(
        dA1,
        sigmoid_derivative_matrix(A1)
    )

    dW1 = multiply(dZ1, T(X))
    dB1 = dZ1

    # Aktualizace parametrů
    W1 = minus(W1, multiply_const(dW1, learning_rate))
    B1 = minus(B1, multiply_const(dB1, learning_rate))

    W2 = minus(W2, multiply_const(dW2, learning_rate))
    B2 = minus(B2, multiply_const(dB2, learning_rate))

    return W1, B1, W2, B2


def train_step(X, Y, W1, B1, W2, B2, learning_rate):

    Z1, A1, Z2, A2 = forward(X, W1, B1, W2, B2)

    W1, B1, W2, B2 = backward(
        X, Y, A1, A2,
        W1, B1, W2, B2,
        learning_rate
    )

    return W1, B1, W2, B2


def train(training_data, epochs, learning_rate,
          W1, B1, W2, B2):

    for epoch in range(epochs):

        random.shuffle(training_data)

        total_loss = 0

        print(f"\nEpoch {epoch + 1}/{epochs}")

        progress = tqdm(training_data, desc="Training", unit="img")

        for path, label in progress:

            X = load_image(path)

            Y = zeros(10, 1)
            Y[label][0] = 1

            # Forward
            Z1, A1, Z2, A2 = forward(
                X, W1, B1, W2, B2
            )

            # Loss
            for i in range(10):
                error = A2[i][0] - Y[i][0]
                total_loss += 0.5 * error ** 2

            # Backward
            W1, B1, W2, B2 = backward(
                X, Y, A1, A2,
                W1, B1, W2, B2,
                learning_rate
            )

            # Aktualizace progress baru
            progress.set_postfix(
                loss=f"{total_loss / (progress.n + 1):.6f}"
            )

        print(
            f"Epoch {epoch + 1}/{epochs}, "
            f"Loss: {total_loss / len(training_data):.6f}"
        )

    return W1, B1, W2, B2

def load_image(path):

    image = Image.open(path)

    image = image.convert("L")
    image = image.resize((256, 256))

    pixels = list(image.get_flattened_data())

    X = zeros(256 * 256, 1)

    for i, pixel in enumerate(pixels):
        X[i][0] = pixel / 255.0

    return X

def load_training_data():

    training_data = []

    dataset_path = os.path.join("cv7", "dataset")

    for table in os.listdir(dataset_path):

        table_path = os.path.join(dataset_path, table)

        if not os.path.isdir(table_path):
            continue

        for label in range(10):

            folder_path = os.path.join(table_path, str(label))

            if not os.path.isdir(folder_path):
                continue

            for filename in os.listdir(folder_path):

                if filename.lower().endswith(".png"):

                    path = os.path.join(folder_path, filename)

                    training_data.append((path, label))

    return training_data


# Uložení vah
def save_weights(W1, B1, W2, B2, filename="weights.txt"):

    data = {
        "W1": W1,
        "B1": B1,
        "W2": W2,
        "B2": B2
    }

    with open(filename, "w") as file:
        json.dump(data, file)

    print("Váhy byly úspěšně uloženy!")


# Načtení vah
def load_weights(filename="weights.txt"):

    with open(filename, "r") as file:
        data = json.load(file)

    W1 = data["W1"]
    B1 = data["B1"]
    W2 = data["W2"]
    B2 = data["B2"]

    print("Váhy byly úspěšně načteny!")

    return W1, B1, W2, B2


if __name__ == "__main__":

    INPUT_SIZE = 256 * 256
    HIDDEN_SIZE = 128
    OUTPUT_SIZE = 10

    # Načtení nebo vytvoření vah
    if os.path.exists("weights.txt"):

        W1, B1, W2, B2 = load_weights()

    else:

        print("Vytvářím nové náhodné váhy...")

        W1 = gen_random_matrix(HIDDEN_SIZE, INPUT_SIZE)
        W2 = gen_random_matrix(OUTPUT_SIZE, HIDDEN_SIZE)

        B1 = zeros(HIDDEN_SIZE, 1)
        B2 = zeros(OUTPUT_SIZE, 1)

    # Načtení datasetu
    training_data = load_training_data()

    print(f"Načteno obrázků: {len(training_data)}")

    if len(training_data) == 0:
        raise ValueError("Dataset neobsahuje žádné obrázky!")

    # Trénování
    W1, B1, W2, B2 = train(
        training_data,
        epochs=5,
        learning_rate=0.0001,
        W1=W1,
        B1=B1,
        W2=W2,
        B2=B2
    )

    # Uložení vah
    save_weights(W1, B1, W2, B2)
