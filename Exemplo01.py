# Aproximação inicial
x1 = 1.25
x2 = 1.3
x3 = 1.4

# Tolerância
erro = 0.01
maxIteracoes = 100

for k in range(maxIteracoes):
    # Gauss-Jacobi:
    # todos os novos valores usam os valores da iteração anterior
    novo_x1 = (10 - x2 - x3) / 8
    novo_x2 = (13 - 2*x1 - x3) / 10
    novo_x3 = (14 - x1 - 2*x2) / 10

    # Maior diferença entre os valores novos e antigos
    maior_erro = max(
        abs(novo_x1 - x1),
        abs(novo_x2 - x2),
        abs(novo_x3 - x3)
    )

    print(f"Iteração {k + 1} | "
          f"x1 = {novo_x1:.6f}, "
          f"x2 = {novo_x2:.6f}, "
          f"x3 = {novo_x3:.6f} "
          f"erro = {maior_erro:.6f}")

    # Atualiza os valores somente depois
    # de calcular todas as incógnitas
    x1 = novo_x1
    x2 = novo_x2
    x3 = novo_x3
    if maior_erro < erro:
        break

print(f"x1 = {x1:.3f}")
print(f"x2 = {x2:.3f}")
print(f"x3 = {x3:.3f}")