import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# INTERPOLAÇÃO DE LAGRANGE
# --------------------------------------------------
def lagrange(x_pontos, y_pontos, x):
    n = len(x_pontos)
    resultado = 0

    for i in range(n):
        termo = y_pontos[i]

        for j in range(n):
            if i != j:
                termo = termo * (
                    (x - x_pontos[j]) /
                    (x_pontos[i] - x_pontos[j])
                )

        resultado = resultado + termo

    return resultado


# --------------------------------------------------
# PLOTAR GRÁFICO
# --------------------------------------------------
def plotar_interpolacao(x_pontos, y_pontos, x_interpolar):

    # Calcula o valor interpolado
    y_interpolado = lagrange(
        x_pontos,
        y_pontos,
        x_interpolar
    )

    # Pontos para desenhar a curva
    x_grafico = np.linspace(
        min(x_pontos),
        max(x_pontos),
        500
    )

    y_grafico = []

    for x in x_grafico:
        y_grafico.append(
            lagrange(x_pontos, y_pontos, x)
        )

    # Gráfico
    plt.figure(figsize=(10, 6))

    plt.plot(
        x_grafico,
        y_grafico,
        label="Polinômio Interpolador"
    )

    plt.scatter(
        x_pontos,
        y_pontos,
        label="Pontos conhecidos"
    )

    plt.scatter(
        x_interpolar,
        y_interpolado,
        s=100,
        label="Ponto interpolado"
    )

    plt.axvline(
        x=x_interpolar,
        linestyle="--"
    )

    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interpolação Polinomial - Lagrange")
    plt.legend()

    plt.show()

    return y_interpolado


# --------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------

x_pontos = []
y_pontos = []

quantidade = int(
    input("Quantidade de pontos conhecidos: ")
)

print("\nDigite os pontos:")

for i in range(quantidade):

    print(f"\nPonto {i + 1}")

    x = float(input("x = "))
    y = float(input("y = "))

    x_pontos.append(x)
    y_pontos.append(y)


x_interpolar = float(
    input("\nValor de x que deseja interpolar: ")
)


resultado = plotar_interpolacao(
    x_pontos,
    y_pontos,
    x_interpolar
)


print("\n-----------------------------")
print("RESULTADO")
print("-----------------------------")

print(
    f"P({x_interpolar}) = {resultado:.6f}"
)