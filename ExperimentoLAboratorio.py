import numpy as np
import matplotlib.pyplot as plt

# Dados simulador de um experimento de laboratório
tempo = np.arange(9, dtype=float)
concentracao = np.array([100, 76, 59, 43, 36, 25, 21, 14, 12], dtype=float)

print(tempo, concentracao)

# Construindo a matriz X
X = np.zeros((len(tempo), 2))
for i, _x in enumerate(tempo):
    X[i] = np.array([_x, 1])

th = np.linalg.inv(X.transpose().dot(X)).dot(X.transpose().dot(concentracao))
print(th)

a = th[0]
b = th[1]

print(f"Coeficiente angular: {a:.4f}")
print(f"Coeficiente linear: {b:.4f}")

print(f"Equação ajustada: y = {a:.4f}x + {b:.4f}")

# Gerando pontos para desenhar a reta
x_reta = np.linspace(0, 8, 100)
y_reta = a * x_reta + b

# Plotando
plt.figure(figsize=(9, 5))

plt.scatter(tempo, concentracao, color="blue", s=80, label="Dados experimentais")
plt.plot(x_reta, y_reta, color="red", linewidth=2, label="Reta ajustada")
plt.title("Experimento: Laboratório")
plt.xlabel("Tempo (dias)")
plt.ylabel("Concetração (ml)")
plt.legend()
plt.grid(True)
plt.show()
