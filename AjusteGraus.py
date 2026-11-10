import numpy as np
import matplotlib.pyplot as plt

def f(x, a, b):
    return (a * x) + b

x = np.linspace(-10, 10, 10)
y = f(x, 2, 1)

X = np.zeros((len(x), 2))
for (i, _x) in enumerate(x):
    X[i] = np.array([_x, 1])


th = np.linalg.inv(X.transpose().dot(X)).dot(X.transpose().dot(y))
print(th)

print("Coeficiente angular (a):", th[0])
print("Coeficiente linear (b):", th[1])

# Calculando os valores da reta ajustad
y_ajustado = th[0] * x + th[1]

# Plotando o gráfic
plt.figure(figsize=(9, 5))

plt.scatter(x, y, color="blue", label="Pontos originais", s=70)
plt.plot(x, y_ajustado, color="red", label="Reta ajustada", linewidth=2)

plt.title("Ajuste de Curvas - Mínimos Quadrados")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid(True)
plt.legend()
plt.show()
