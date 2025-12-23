import requests
import matplotlib.pyplot as plt
import os

OEIS_id = 'A014847'

def bfile_url(OEIS_id):
    OEIS_url = 'https://oeis.org'
    OEIS_id = OEIS_id.upper()
    bfile = 'b' + OEIS_id[1:] + '.txt'
    url = f"{OEIS_url}/{OEIS_id}/{bfile}"
    return url

url = bfile_url(OEIS_id)

response = requests.get(url)
response.raise_for_status()

# Parsear datos directamente desde texto en memoria
data = []
for line in response.text.splitlines():
    if line.startswith('#') or line.strip() == '':
        continue
    parts = line.strip().split()
    if len(parts) == 2:
        n, val = parts
        data.append((int(n), int(val)))

# Separar en listas para graficar
n_values, vals = zip(*data)

# Aplicar estilo ggplot
plt.style.use('ggplot')

plt.figure(figsize=(10, 6))
plt.plot(n_values, vals, marker='o', linestyle='-', color='steelblue', linewidth=2, markersize=2)
plt.title(f'{OEIS_id}(n)', fontsize=16, weight='bold')
plt.xlabel('n', fontsize=14)
#plt.ylabel('Valor', fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()

# Directorio actual de trabajo (desde donde se ejecuta el script)
ruta_actual = os.getcwd()

# Guardar imagen PNG en directorio actual
img_path = os.path.join(ruta_actual, f'{OEIS_id}_plot.png')
plt.savefig(img_path, dpi=300)
plt.close()

print(f"Gráfica guardada en: {img_path}")

