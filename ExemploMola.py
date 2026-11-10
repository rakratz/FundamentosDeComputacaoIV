import numpy as np
import matplotlib.pyplot as plt

# Dados obtidos no experiment
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0.2, 1.8, 4.3, 5.9, 8.2, 9.7])

print(x,y)

# Construindo a matriz X
X = np.zeros((len(x), 2))

for i, _x in enumerate(x):
    X[i] = np.array([_x, 1])

th = np.linalg.inv(X.transpose().dot(X)).dot(X.transpose().dot(y))
print(th)

a = th[0]
b = th[1]

print(f"Coeficiente angular: {a:.4f}")
print(f"Coeficiente linear: {b:.4f}")

print(f"Equação ajustada: y = {a:.4f}x + {b:.4f}")

# Gerando pontos para desenhar a reta
x_reta = np.linspace(0, 5, 100)
y_reta = a * x_reta + b


# Plotando
plt.figure(figsize=(9, 5))

plt.scatter(x, y, color="blue", s=80, label="Dados experimentais")
plt.plot(x_reta, y_reta, color="red", linewidth=2, label="Reta ajustada")
plt.title("Experimento: Alongamento de uma Mola")
plt.xlabel("Força aplicada (N)")
plt.ylabel("Alongamento (cm)")
plt.legend()
plt.grid(True)
plt.show()
