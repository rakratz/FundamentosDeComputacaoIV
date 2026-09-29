import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


# --------------------------------------------------
# MÉTODO DA BISSECÇÃO
# --------------------------------------------------
def bisseccao(f, a, b, tol=1e-5):

    # Calcula os valores nos extremos
    fa = f(a)
    fb = f(b)

    # Verifica se a já é uma raiz
    if abs(fa) < tol:
        return a

    # Verifica se b já é uma raiz
    if abs(fb) < tol:
        return b

    # Verifica se existe mudança de sinal
    if fa * fb > 0:
        return None

    # Processo iterativo
    while abs(b - a) > tol:

        # Ponto médio
        m = (a + b) / 2

        fm = f(m)

        # Verifica se encontrou uma aproximação da raiz
        if abs(fm) < tol:
            return m

        # Escolhe o novo intervalo
        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm

    # Retorna o ponto médio final
    return (a + b) / 2


# --------------------------------------------------
# PLOTAR FUNÇÃO
# --------------------------------------------------
def plotar_funcao(f, inicio, fim, raiz=None):

    x = np.linspace(inicio, fim, 500)
    y = f(x)

    plt.figure(figsize=(10, 5))

    # Gráfico da função
    plt.plot(x, y, label="f(x)")

    # Eixos
    plt.axhline(0, linewidth=1)
    plt.axvline(0, linewidth=1)

    # Marca a raiz encontrada
    if raiz is not None:
        plt.scatter(
            raiz,
            0,
            s=100,
            label=f"Raiz = {raiz:.5f}"
        )

    plt.grid(True)
    plt.legend()

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Gráfico da função")

    plt.show()


# --------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------

print("====================================")
print("       RAÍZES DE EQUAÇÕES")
print("====================================")

print("\nExemplos de funções:")
print("x**2 - 4")
print("x**3 - 4*x - 1")
print("sin(x) - 0.5")
print("exp(-x) - x")


# --------------------------------------------------
# DEFINIÇÃO DA FUNÇÃO
# --------------------------------------------------

# Cria a variável simbólica
x = sp.symbols("x")


# Usuário informa a função
equacao = input("\nDigite f(x): ")


# Aceita X maiúsculo
equacao = equacao.replace("X", "x")


# Converte o texto para uma expressão matemática
expressao = sp.sympify(equacao)


# Converte a expressão simbólica para função numérica
f = sp.lambdify(x, expressao, "numpy")


print("\nFunção informada:")
print("f(x) =", expressao)


# --------------------------------------------------
# INTERVALO DO GRÁFICO
# --------------------------------------------------

print("\n--- Intervalo do gráfico ---")

inicio = float(input("Início: "))
fim = float(input("Fim: "))


# --------------------------------------------------
# INTERVALO DA BISSECÇÃO
# --------------------------------------------------

print("\n--- Intervalo para procurar a raiz ---")

a = float(input("a = "))
b = float(input("b = "))


# --------------------------------------------------
# CALCULAR A RAIZ
# --------------------------------------------------

raiz = bisseccao(f, a, b)


# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("\n====================================")
print("             RESULTADO")
print("====================================")


if raiz is not None:

    print(f"Raiz aproximada: {raiz:.6f}")
    print(f"f(raiz): {f(raiz):.10f}")

else:

    print("Não foi possível aplicar a bissecção.")

    print(f"\nf({a}) = {f(a):.6f}")
    print(f"f({b}) = {f(b):.6f}")

    print("\nNão existe mudança de sinal no intervalo.")
    print("Escolha valores de a e b onde")
    print("f(a) e f(b) tenham sinais diferentes.")


# --------------------------------------------------
# GRÁFICO
# --------------------------------------------------

plotar_funcao(
    f,
    inicio,
    fim,
    raiz
)