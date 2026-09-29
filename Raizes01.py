import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# FUNÇÃO QUE DESEJAMOS ENCONTRAR A RAIZ
# --------------------------------------------------
def f(x):
    return x**3 - 4*x - 1


# --------------------------------------------------
# MÉTODO DA BISSEÇÃO
# --------------------------------------------------
def bisseccao(f, a, b, tol=1e-5):

    # Verifica se existe mudança de sinal
    if f(a) * f(b) >= 0:
        print("Não existe mudança de sinal no intervalo.")
        return None

    # Repete até atingir a tolerância
    while abs(b - a) > tol:

        # Calcula o ponto médio
        m = (a + b) / 2

        # Encontrou exatamente a raiz
        if f(m) == 0:
            return m

        # Verifica em qual metade está a raiz
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

    # Retorna a aproximação da raiz
    return (a + b) / 2


# --------------------------------------------------
# GRÁFICO DA FUNÇÃO
# --------------------------------------------------
def plotar_funcao(f, inicio, fim):

    x = np.linspace(inicio, fim, 500)
    y = f(x)

    plt.figure(figsize=(10, 5))

    plt.plot(x, y, label="f(x)")

    plt.axhline(0, linewidth=1)
    plt.axvline(0, linewidth=1)

    plt.grid(True)
    plt.legend()

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Gráfico da função")

    plt.show()


# --------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------

# Mostra o gráfico
plotar_funcao(f, -3, 3)


# Intervalo escolhido para procurar a raiz
a = -1
b = 0


# Calcula a raiz
raiz = bisseccao(f, a, b)


# Mostra o resultado
if raiz is not None:
    print("Raiz aproximada:", raiz)
    print("f(raiz):", f(raiz))
else:
    print("Não foi possível encontrar a raiz nesse intervalo.")