import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# INTERPOLAÇÃO POLINOMIAL DE LAGRANGE
# --------------------------------------------------
def lagrange(x_pontos, y_pontos, x):

    resultado = 0
    n = len(x_pontos)

    # Percorre todos os pontos conhecidos
    for i in range(n):

        termo = y_pontos[i]

        # Calcula o termo de Lagrange
        for j in range(n):

            if i != j:
                termo *= (
                    (x - x_pontos[j]) /
                    (x_pontos[i] - x_pontos[j])
                )

        resultado += termo

    return resultado


# --------------------------------------------------
# PONTOS CONHECIDOS
# --------------------------------------------------

x_pontos = [0, 1, 2, 3]
y_pontos = [1, 3, 2, 5]


# --------------------------------------------------
# VALOR QUE DESEJAMOS INTERPOLAR
# --------------------------------------------------

valor = 1.7

resultado = lagrange(
    x_pontos,
    y_pontos,
    valor
)


# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("==============================")
print("   INTERPOLAÇÃO DE LAGRANGE")
print("==============================")

print("\nPontos conhecidos:")

for i in range(len(x_pontos)):
    print(f"({x_pontos[i]}, {y_pontos[i]})")

print(f"\nValor de x: {valor}")
print(f"P({valor}) = {resultado:.6f}")


# --------------------------------------------------
# PREPARAR O GRÁFICO
# --------------------------------------------------

x_grafico = np.linspace(
    min(x_pontos),
    max(x_pontos),
    300
)

y_grafico = [
    lagrange(x_pontos, y_pontos, x)
    for x in x_grafico
]


# --------------------------------------------------
# GRÁFICO
# --------------------------------------------------

plt.figure(figsize=(10, 5))

# Polinômio interpolador
plt.plot(
    x_grafico,
    y_grafico,
    label="Polinômio interpolador"
)

# Pontos conhecidos
plt.scatter(
    x_pontos,
    y_pontos,
    s=80,
    label="Pontos conhecidos"
)

# Valor interpolado
plt.scatter(
    valor,
    resultado,
    s=100,
    label=f"P({valor}) = {resultado:.3f}"
)

# Eixos
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)

plt.grid(True)
plt.legend()

plt.xlabel("x")
plt.ylabel("y")

plt.title(
    "Interpolação Polinomial de Lagrange"
)

plt.show()