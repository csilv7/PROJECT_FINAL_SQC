# -------------
# [1] Exemplo 1
# -------------

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Parâmetros
k = 25  # Número de Amostras
n = 5   # Tamanho de cada Amostra

# Simular dados com semente de aleatoriedade para reprodutibilidade
np.random.seed(42)
vec_data = np.random.normal(loc=25, scale=1.5, size=k*n) + np.random.normal(loc=0, scale=1.2, size=k*n)

# Organizar a matriz de dados
matrix_data = vec_data.reshape(k, n)

# Vetor de médias (média de cada linha)
vec_means = matrix_data.mean(axis=1)

# Vetor de desvios (desvio padrão amostral de cada linha, ddof=1)
vec_sds = matrix_data.std(axis=1, ddof=1)

# Estimar quantidades
x_bar = vec_means.mean()
x_std = 1.5

# Construir limites
lic = x_bar - (3 / np.sqrt(n)) * x_std  # Limite Inferior de Controle
lc  = 25                               # Limite Central
lsc = x_bar + (3 / np.sqrt(n)) * x_std  # Limite Superior de Controle

# Configurar o estilo do gráfico
sns.set_theme(style="ticks") # Similar ao theme_classic()

# Configurações de Figura
fig, ax = plt.subplots(figsize=(5, 3), dpi=800)

sns.lineplot(x=range(1, k+1), y=vec_means, marker="o", color="black", ax=ax)

# Plotar as linhas de controle
ax.axhline(y=lsc, color="red", linestyle="-", label=f"LSC = {lsc:.2f}")
ax.axhline(y=lc, color="blue", linestyle="-", label=f"$\\hat{{\\mu}}$ = {lc:.2f}") # Usando LaTeX para mu
ax.axhline(y=lic, color="red", linestyle="-", label=f"LIC = {lic:.2f}")

# Configurações de eixos e títulos
ax.set_ylim(18, 32)
ax.set_xlabel("Amostra", weight="bold", fontsize=12)
ax.set_ylabel("Medida", weight="bold", fontsize=12)

# Configurações de Legenda
ax.legend(prop={"size":8, "weight": "bold"}, loc="upper right", frameon=False) # bbox_to_anchor=(1, 0.5), 

# Outras configurações
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Exibição da Figura
plt.show()

# -------------
# [2] Exemplo 2
# -------------

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tbl61 = np.array([
    [1, 1.3235, 1.4128, 1.6744, 1.4573],
    [2, 1.4314, 1.3592, 1.6075, 1.4666],
    [3, 1.4284, 1.4871, 1.4932, 1.4324],
    [4, 1.5028, 1.6352, 1.3841, 1.2831],
    [5, 1.5604, 1.2735, 1.5265, 1.4362],
    [6, 1.5955, 1.5451, 1.3574, 1.3281],
    [7, 1.6274, 1.5064, 1.8366, 1.4177],
    [8, 1.4190, 1.4303, 1.6637, 1.6067],
    [9, 1.3884, 1.7277, 1.5355, 1.5176],
    [10, 1.4039, 1.6697, 1.5089, 1.6477],
    [11, 1.4158, 1.7667, 1.4278, 1.5927],
    [12, 1.5821, 1.3355, 1.5777, 1.3908],
    [13, 1.2856, 1.4106, 1.4447, 1.6388],
    [14, 1.4951, 1.4036, 1.5893, 1.6458],
    [15, 1.3589, 1.2863, 1.5996, 1.2497],
    [16, 1.5747, 1.5301, 1.5171, 1.1839],
    [17, 1.3680, 1.7269, 1.3957, 1.5019],
    [18, 1.4163, 1.3864, 1.3057, 1.6210],
    [19, 1.5796, 1.4185, 1.6541, 1.5116],
    [20, 1.7106, 1.4412, 1.2361, 1.3824],
    [21, 1.4371, 1.5051, 1.3485, 1.5670],
    [22, 1.4738, 1.5936, 1.6583, 1.4973],
    [23, 1.5917, 1.4333, 1.5551, 1.5295],
    [24, 1.6399, 1.5243, 1.5705, 1.5563],
    [25, 1.5797, 1.3663, 1.6240, 1.3732]
])

# Obter apenas as amostras
samples_x = tbl61[, 1:]