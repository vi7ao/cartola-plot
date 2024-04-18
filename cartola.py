import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

vitaoPoints = [55.1, 59.25, 60.39, 77.0, 84.27, 55.14, 58.84, 45.03, 75.64, 51.34, 41.65, 39.13, 54.20,
                65.14, 59.16, 58.67, 89.06, 38.40, 79.0, 72.02, 72.0, 61.54, 52.0, 55.86, 55.69, 59.41,
                51.31, 81.08, 60.14, 94.30, 72.36, 49.48, 41.43, 96.66, 97.51, 104.06, 88.62, 47.01]
louPoints = [43.70, 55.40, 47.53, 60.14, 86.01, 60.83, 69.85, 58.40, 59.14, 83.37, 62.82, 60.78, 81.15,
             58.41, 84.71, 53.85, 66.77, 26.00, 69.46, 76.12, 90.39, 72.49, 48.40, 55.89, 74.54, 50.34,
             40.01, 68.48, 71.14, 67.93, 58.11, 60.15, 34.76, 91.00, 95.69, 61.11, 71.82, 49.83]
ewePoints = [83.70, 38.70, 34.27, 36.28, 73.53, 54.47, 75.91, 67.90, 83.49, 64.65, 50.29, 40.35, 60.50,
             35.14, 82.02, 39.95, 58.85, 26.31, 77.16, 58.12, 74.05, 57.08, 68.40, 58.68, 73.19, 57.42,
             23.25, 56.04, 89.79, 64.39, 60.01, 76.10, 30.40, 69.25, 72.44, 92.26, 81.90, 42.98]
jorgaoPoints = [0.0, 31.92, 63.06, 34.33, 55.88, 53.75, 51.66, 32.39, 46.33, 48.19, 60.76, 68.51, 54.70,
                45.82, 67.01, 23.34, 77.35, 38.94, 54.59, 49.57, 83.28, 50.80, 48.52, 53.45, 28.15, 32.00,
                37.65, 77.10, 85.30, 86.22, 61.52, 43.04, 66.40, 48.43, 119.37, 82.57, 56.01, 43.53]

vitaoAcumulado = np.cumsum(vitaoPoints)
louAcumulado = np.cumsum(louPoints)
eweAcumulado = np.cumsum(ewePoints)
jorgaoAcumulado = np.cumsum(jorgaoPoints)

plt.plot(vitaoAcumulado, label="Vitão")
plt.plot(louAcumulado, label="Lou")
plt.plot(eweAcumulado, label="Ewe")
plt.plot(jorgaoAcumulado, label="Jorgão")

plt.title("LOS TELES CARTOLA FC 2023")
plt.xlabel("Rodada")
plt.ylabel("Pontuação")
plt.legend(["Vitão", "Lou", "Ewe", "Jorgão"])
plt.grid(True)
plt.show()

plt.hist(vitaoPoints, bins=50, alpha=0.5, label='Vitao')
plt.hist(louPoints, bins=50, alpha=0.5, label='Lou')
plt.hist(ewePoints, bins=50, alpha=0.5, label='Ewe')
plt.hist(jorgaoPoints, bins=50, alpha=0.5, label='Jorgao')

plt.title('Histograma de Pontuações')
plt.xlabel('Pontuação')
plt.ylabel('Frequência')
plt.legend()

plt.show()

vitao_mean = np.mean(vitaoPoints)
lou_mean = np.mean(louPoints)
ewe_mean = np.mean(ewePoints)
jorgao_mean = np.mean(jorgaoPoints)

vitao_median = np.median(vitaoPoints)
lou_median = np.median(louPoints)
ewe_median = np.median(ewePoints)
jorgao_median = np.median(jorgaoPoints)

vitao_std = np.std(vitaoPoints)
lou_std = np.std(louPoints)
ewe_std = np.std(ewePoints)
jorgao_std = np.std(jorgaoPoints)

print("Estatísticas Descritivas:")
print(f"Vitão - Média: {vitao_mean:.2f}, Mediana: {vitao_median:.2f}, Desvio Padrão: {vitao_std:.2f}")
print(f"Lou - Média: {lou_mean:.2f}, Mediana: {lou_median:.2f}, Desvio Padrão: {lou_std:.2f}")
print(f"Ewe - Média: {ewe_mean:.2f}, Mediana: {ewe_median:.2f}, Desvio Padrão: {ewe_std:.2f}")
print(f"Jorgão - Média: {jorgao_mean:.2f}, Mediana: {jorgao_median:.2f}, Desvio Padrão: {jorgao_std:.2f}")

df = pd.DataFrame({
    'Vitao': vitaoPoints,
    'Lou': louPoints,
    'Ewe': ewePoints,
    'Jorgao': jorgaoPoints
})
alpha = 0.2  #fator de suavização
df_smooth = df.ewm(alpha=alpha).mean()

plt.figure(figsize=(12, 6))
plt.plot(df, marker='o', linestyle='-', alpha=0.5)
plt.title('Pontuações')
plt.xlabel('Rodada')
plt.ylabel('Pontuação')
plt.legend(['Vitao', 'Lou', 'Ewe', 'Jorgao'])
plt.grid(True)
plt.show()

df_relative = df.subtract(df.max(axis=1), axis=0)

plt.figure(figsize=(12, 6))
plt.plot(df_relative, marker='o', linestyle='-')
plt.title('Desempenho Relativo em Relação ao Líder')
plt.xlabel('Rodada')
plt.ylabel('Desempenho Relativo')
plt.legend(['Vitao', 'Lou', 'Ewe', 'Jorgao'])
plt.grid(True)
plt.show()

best_player_counts = df.idxmax(axis=1).value_counts()

plt.bar(best_player_counts.index, best_player_counts.values)
plt.title('Número de Vezes que Cada Jogador Foi o Melhor da Rodada')
plt.xlabel('Jogador')
plt.ylabel('Número de Vezes')
plt.grid(axis='y')
plt.show()

worst_player = df.idxmin(axis=1)

worst_player_counts = worst_player.value_counts()

plt.bar(worst_player_counts.index, worst_player_counts.values)
plt.title('Lanterna da Rodada')
plt.xlabel('Jogador')
plt.ylabel('Número de Vezes')
plt.grid(axis='y')
plt.show()

over_70_counts = (df > 70).sum()

plt.bar(over_70_counts.index, over_70_counts.values)
plt.title('MITADAS (mais de 70 Pontos)')
plt.xlabel('Jogador')
plt.ylabel('Número de Vezes')
plt.grid(axis='y')
plt.show()

under_40_counts = (df < 40).sum()

plt.bar(under_40_counts.index, under_40_counts.values)
plt.title('CAGADAS (menos de 40 pontos')
plt.xlabel('Jogador')
plt.ylabel('Número de Vezes')
plt.grid(axis='y')
plt.show()