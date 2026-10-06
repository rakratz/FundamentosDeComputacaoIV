import numpy as np
import matplotlib.pyplot as plt

def newton(x_pontos, y_pontos, x):
    n = len(x_pontos)

    # Copia os valores de y
    coef = y_pontos.copy()

    # Calcula as diferenças divididas
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / \
                      (x_pontos[i] - x_pontos[i - j])

    # Calcula P(x)
    resultado = coef[0]
    produto = 1

    for i in range(1, n):
        produto *= (x - x_pontos[i - 1])
        resultado += coef[i] * produto

    return resultado
