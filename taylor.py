import numpy as np
import math
import matplotlib.pyplot as plt

def termo(x, n):
  return (x**n)/math.factorial(n)

def taylor(x, N):
  y = np.zeros_like(x, dtype=float)
  for n in range(N):
    y += termo(x, n)    # soma 1, depois x, x^2/2! + ....
  return y

x = np.linspace(0, 4, 400)  # [0, 0.0103 , 0.2005, ... ... 2.0012.. 4]
N = int(input("Números de Termos: "))
plt.figure(figsize=(10,6))

for n in range(1, N + 1):
  y = taylor(x, n)
  plt.plot(x, y, label=f'n - {n}')

plt.plot(x, np.exp(x), 'k-', linewidth=2, label='e^x')
plt.title('Aproximação de e^x (Série de Taylor), a = 0')
plt.xlabel('x')
plt.ylabel('e^x')
plt.axhline(0, linewidth=0.5)
plt.axvline(0, linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()
print(f"Aproximação de Taylor = {y}")