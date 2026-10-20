
import numpy as np

# ============================================================
# 1. ESCOLHA DO TIPO DE ENTRADA
# ============================================================

# O usuário pode informar uma função matemática diretamente
# ou carregar os valores de uma função a partir de um arquivo .txt.

modo = int(input("Entrada: 1-função | 2-arquivo .txt: "))

if modo == 1:

    # Recebe a expressão matemática.
    # Exemplo: x**2 + 3*x
    # Exemplo: np.sin(x)
    # Exemplo: np.sqrt(x**2 + 1) / np.sin(x)

    expr = input("f(x) = ")

    # Cria uma função Python a partir da expressão digitada.
    # lambda permite definir uma função de forma simplificada.
    # eval interpreta a expressão matemática informada.
    # Utilize apenas expressões de fontes confiáveis.

    f = lambda x: eval(expr, {"__builtins__": {}},
                       {"x": x, "np": np})


elif modo == 2:

    # Solicita o nome do arquivo contendo os dados.
    # O arquivo deve possuir duas colunas:
    # primeira coluna = x
    # segunda coluna = f(x)

    nome = input("Arquivo (.txt): ")

    # Carrega os dados do arquivo.
    dados = np.loadtxt(nome)

    # Separa os valores de x e f(x).
    x_tab = dados[:, 0]
    y_tab = dados[:, 1]

else:
    print("Modo inválido!")
    exit()


# ============================================================
# 2. ENTRADA DOS PARÂMETROS
# ============================================================

# Ponto onde queremos calcular a derivada.
x = float(input("x = "))

# Passo h: distância entre os pontos utilizados.
h = float(input("h = "))

# Ordem da derivada:
# 1 = primeira derivada
# 2 = segunda derivada
# 3 = terceira derivada
# 4 = quarta derivada
n = int(input("Ordem (1-4): "))

# Método numérico:
# 1 = progressivo (pontos à frente)
# 2 = regressivo (pontos anteriores)
# 3 = centrado (pontos dos dois lados)
t = int(input("Tipo (1=prog, 2=reg, 3=cent): "))

# Verifica se os parâmetros são válidos.
if h <= 0 or n not in (1, 2, 3, 4) or t not in (1, 2, 3):
    print("Parâmetros inválidos!")
    exit()


# ============================================================
# 3. FUNÇÃO PARA CONSULTAR VALORES TABELADOS
# ============================================================

# Esta função será utilizada apenas no modo 2.
# Ela procura um valor de x dentro da tabela carregada.

def f_tab(xp):

    # np.isclose compara valores considerando
    # pequenas diferenças de representação decimal.
    # np.where retorna as posições encontradas.

    idx = np.where(np.isclose(x_tab, xp))[0]

    # Se o ponto não estiver na tabela,
    # não será possível calcular a função nele.
    if len(idx) == 0:
        raise ValueError("Ponto não está na tabela")

    # Retorna o valor de f(x) correspondente.
    return y_tab[idx[0]]


# Se o usuário escolheu trabalhar com tabela,
# a função f passa a consultar os dados do arquivo.
if modo == 2:
    f = f_tab


# ============================================================
# 4. VERIFICAÇÃO DOS PONTOS NECESSÁRIOS
# ============================================================

# Cada derivada e cada método exigem pontos específicos.
#
# Exemplo:
# Primeira derivada progressiva: x e x+h
# Primeira derivada regressiva: x e x-h
# Primeira derivada centrada: x-h e x+h
#
# Esta função verifica se os pontos necessários
# podem ser avaliados.

def pode_calcular(x, h, n, t):

    # Dicionário com os pontos necessários.
    #
    # Primeiro índice: ordem da derivada.
    # Segundo índice: tipo do método.

    pontos = {

        # PRIMEIRA DERIVADA
        1: {
            1: [x, x+h],
            2: [x, x-h],
            3: [x-h, x+h]
        },

        # SEGUNDA DERIVADA
        2: {
            1: [x, x+h, x+2*h],
            2: [x, x-h, x-2*h],
            3: [x-h, x, x+h]
        },

        # TERCEIRA DERIVADA
        3: {
            1: [x, x+h, x+2*h, x+3*h],
            2: [x, x-h, x-2*h, x-3*h],
            3: [x-2*h, x-h, x+h, x+2*h]
        },

        # QUARTA DERIVADA
        4: {
            1: [x, x+h, x+2*h, x+3*h, x+4*h],
            2: [x, x-h, x-2*h, x-3*h, x-4*h],
            3: [x-2*h, x-h, x, x+h, x+2*h]
        }
    }

    try:

        # Percorre os pontos necessários.
        for xp in pontos[n][t]:

            # Tenta calcular a função no ponto.
            valor = f(xp)

            # Verifica se o resultado é um número finito.
            if not np.isfinite(valor):
                return False

        # Todos os pontos foram avaliados.
        return True

    except (ValueError, ZeroDivisionError, OverflowError,
            FloatingPointError, TypeError, IndexError, KeyError):

        # Algum ponto não pôde ser avaliado.
        return False


# Verifica se o cálculo pode ser realizado.
if not pode_calcular(x, h, n, t):

    print("Não é possível calcular com esses dados/método.")
    exit()


# ============================================================
# 5. FÓRMULAS DAS DERIVADAS NUMÉRICAS
# ============================================================

# O dicionário D armazena todas as fórmulas.
#
# D[1] = primeira derivada
# D[2] = segunda derivada
# D[3] = terceira derivada
# D[4] = quarta derivada
#
# Dentro de cada lista:
# posição 0 = progressiva
# posição 1 = regressiva
# posição 2 = centrada
#
# lambda f,x,h define cada fórmula matemática.

D = {

    # --------------------------------------------------------
    # PRIMEIRA DERIVADA
    # --------------------------------------------------------

    1: [

        # Progressiva:
        # f'(x) ≈ [f(x+h) - f(x)] / h

        lambda f,x,h:
            (f(x+h) - f(x)) / h,

        # Regressiva:
        # f'(x) ≈ [f(x) - f(x-h)] / h

        lambda f,x,h:
            (f(x) - f(x-h)) / h,

        # Centrada:
        # f'(x) ≈ [f(x+h) - f(x-h)] / (2h)

        lambda f,x,h:
            (f(x+h) - f(x-h)) / (2*h)
    ],


    # --------------------------------------------------------
    # SEGUNDA DERIVADA
    # --------------------------------------------------------

    2: [

        # Progressiva

        lambda f,x,h:
            (f(x+2*h) - 2*f(x+h) + f(x)) / h**2,

        # Regressiva

        lambda f,x,h:
            (f(x) - 2*f(x-h) + f(x-2*h)) / h**2,

        # Centrada

        lambda f,x,h:
            (f(x+h) - 2*f(x) + f(x-h)) / h**2
    ],


    # --------------------------------------------------------
    # TERCEIRA DERIVADA
    # --------------------------------------------------------

    3: [

        # Progressiva

        lambda f,x,h:
            (f(x+3*h) - 3*f(x+2*h)
             + 3*f(x+h) - f(x)) / h**3,

        # Regressiva

        lambda f,x,h:
            (f(x) - 3*f(x-h)
             + 3*f(x-2*h) - f(x-3*h)) / h**3,

        # Centrada

        lambda f,x,h:
            (f(x+2*h) - 2*f(x+h)
             + 2*f(x-h) - f(x-2*h)) / (2*h**3)
    ],


    # --------------------------------------------------------
    # QUARTA DERIVADA
    # --------------------------------------------------------

    4: [

        # Progressiva

        lambda f,x,h:
            (f(x+4*h) - 4*f(x+3*h)
             + 6*f(x+2*h) - 4*f(x+h)
             + f(x)) / h**4,

        # Regressiva

        lambda f,x,h:
            (f(x) - 4*f(x-h)
             + 6*f(x-2*h) - 4*f(x-3*h)
             + f(x-4*h)) / h**4,

        # Centrada

        lambda f,x,h:
            (f(x+2*h) - 4*f(x+h)
             + 6*f(x) - 4*f(x-h)
             + f(x-2*h)) / h**4
    ]
}


# ============================================================
# 6. CÁLCULO DA DERIVADA
# ============================================================

# Seleciona a fórmula correspondente à ordem e ao método.
#
# Exemplo:
# n = 2 -> segunda derivada
# t = 3 -> método centrado
#
# D[2][2] seleciona a segunda derivada centrada.
#
# Usamos t-1 porque os índices começam em zero.

d = D[n][t-1](f, x, h)


# ============================================================
# 7. EXIBIÇÃO DO RESULTADO
# ============================================================

# Identifica o método escolhido.
metodos = {
    1: "Progressivo",
    2: "Regressivo",
    3: "Centrado"
}

print("\n========== RESULTADO ==========")

print(f"Ponto x = {x}")
print(f"Passo h = {h}")
print(f"Ordem da derivada = {n}")
print(f"Método = {metodos[t]}")

# .6e representa o resultado em notação científica.
print(f"\nD^{n}f(x) = {d:.6e}")

# .6f representa o resultado em formato decimal.
print(f"Valor aproximado = {d:.6f}")

print("================================")
