import numpy as np
import matplotlib.pyplot as plt

def newton(x_pontos, y_pontos, x):
    n = len(x_pontos)

    # Copia os valores de y
    coef = y_pontos.copy()

    # Calcula as diferenças divididas
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) \ (x_pontos[i] - x_pontos[i - j])

    # Calcula P(x)
    resultado = coef[0]
    produto = 1

    for i in range(1, n):
        produto *= (x - x_pontos[i - 1])
        resultado += coef[i] * produto

    return resultado


# -------------------------
# Pontos conhecidos
# -------------------------

x_pontos = [1, 2, 3]
y_pontos = [1, 4, 9]


# -------------------------
# Plotagem
# -------------------------

# Valores de x para desenhar a curva
x = np.linspace(0, 4, 100)

# Calcula P(x) para cada valor
y = newton(x_pontos, y_pontos, x)

# Desenha o polinômio
plt.plot(x, y, label="Polinômio de Newton")

# Desenha os pontos conhecidos
plt.scatter(x_pontos, y_pontos, label="Pontos conhecidos")

plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("Interpolação pelo Polinômio de Newton")
plt.grid()
plt.legend()

plt.show()
