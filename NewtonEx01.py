import numpy as np
import matplotlib.pyplot as plt

x0 = 1
x1 = 2
x2 = 3

y0 = 1
y1 = 4
y2 = 9

# Diferenças divididas de primeira ordem
d01 = (y1 - y0) / (x1 - x0)
d12 = (y2 - y1) / (x2 - x1)

# Diferença dividida de segunda ordem
d012 = (d12 - d01) / (x2 - x0)

print("a0 =", y0)
print("a1 =", d01)
print("a2 =", d012)


# Polinômio interpolador de Newton
def P(x):
    return y0 + d01*(x - x0) + d012*(x - x0)*(x - x1)


# Valores para desenhar a curva
x = np.linspace(0, 4, 100)
y = P(x)

# Plotar o polinômio
plt.plot(x, y, label="Polinômio de Newton")

# Plotar os pontos conhecidos
plt.scatter([x0, x1, x2], [y0, y1, y2],
            label="Pontos conhecidos")

plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("Interpolação pelo Polinômio de Newton")
plt.grid()
plt.legend()

plt.show()