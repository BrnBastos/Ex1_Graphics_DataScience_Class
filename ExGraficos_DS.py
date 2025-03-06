# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 00:09:59 2025

@author: bruni
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'dataset_clima.csv'
df = pd.read_csv(file_path)

# Garantir a ordem correta dos meses para agrupamento
ordem_meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
df['Mês'] = pd.Categorical(df['Mês'], categories=ordem_meses, ordered=True)

# Calcular médias mensais para todo o período disponível
df_mensal = df.groupby('Mês').mean().reset_index()

# Converter os meses em índices para facilitar a plotagem
x = np.arange(len(df_mensal['Mês']))

# Criar figura com três gráficos
fig, ax = plt.subplots(3, 1, figsize=(10, 12))

# Gráfico 1: Temperatura Média por Mês
ax[0].plot(x, df_mensal['Temperatura_Média'], color='orange', marker='o')
ax[0].set_title("Temperatura Média por Mês (Média Anual)")
ax[0].set_ylabel("Temperatura (°C)")
ax[0].set_xticks(x)
ax[0].set_xticklabels(df_mensal['Mês'])
ax[0].grid(True, linestyle='--', alpha=0.5)

# Gráfico 2: Precipitação por Mês
ax[1].plot(x, df_mensal['Precipitação_mm'], color='blue', marker='s')
ax[1].set_title("Precipitação por Mês (Média Anual)")
ax[1].set_ylabel("Precipitação (mm)")
ax[1].set_xticks(x)
ax[1].set_xticklabels(df_mensal['Mês'])
ax[1].grid(True, linestyle='--', alpha=0.5)

# Gráfico 3: Umidade Relativa por Mês
ax[2].plot(x, df_mensal['Umidade_Relativa_%'], color='green', marker='^')
ax[2].set_title("Umidade Relativa por Mês (Média Anual)")
ax[2].set_ylabel("Umidade (%)")
ax[2].set_xticks(x)
ax[2].set_xticklabels(df_mensal['Mês'])
ax[2].grid(True, linestyle='--', alpha=0.5)

# Ajustar layout e exibir os gráficos
plt.tight_layout()
plt.show()
