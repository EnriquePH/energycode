import matplotlib.pyplot as plt
from sympy import fibonacci, factorint
import numpy as np

N_MAX = 120

# Calcular omega(F_n) para n en un rango
n_vals = list(range(1, N_MAX + 1))  # desde F_1 hasta F_100
omega_vals = []

# omega(F_n): número de factores primos distintos
for n in n_vals:
    Fn = fibonacci(n)
    factors = factorint(Fn)
    omega_vals.append(len(factors))

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(n_vals, omega_vals, marker='o', linestyle='-', color='teal')
plt.title(f"Número de factores primos distintos (ω) de F_n para 1 ≤ n ≤ {N_MAX}")
plt.xlabel("n")
plt.ylabel(r"$\omega(F_n)$")
plt.grid(True)
plt.show()
