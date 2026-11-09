# vytvorte program ktery pozna ze je na obrazku pes, kocka, ryba
import math
from matrix import T, multiply, apply, plus

def signoid(x):
    return 1 / (1 + math.exp(-x))

def neuron_network(
        X
):
    X = T(X)
    W = [
        [0.4, 0.1, 0.3, 0.4, 0.1, 0.5, -0.2], #dog
        [-0.2, -0.2, 0.1, 0.1, 0.1, 0.1, 0.6], #fish
        [0.4, 0.3, 0.5, 0.5, 0.5, 0.3, 0.0] #cat
    ]

    b = T([[0.1, 0.1, 0.1]]) # bias

    result = multiply(W, X)
    result = plus(result, b)

    return apply(result, signoid)


def do_softmax(items):
    total_signoid = sum(items)
    for index, i in enumerate(items):
        print(f"{index} -> {i / total_signoid}")

if __name__ == "__main__":
    X = [
        [0.75, 1, 1, 1, 1, 1, 0] # priznaky/vstup
    ]

    print(neuron_network(
        X
    ))