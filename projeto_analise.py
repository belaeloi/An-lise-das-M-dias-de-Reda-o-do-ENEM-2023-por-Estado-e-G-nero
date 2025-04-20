import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo CSV
caminho = r"C:\Users\isabela\Downloads\microdados_enem_2023\DADOS\MICRODADOS_ENEM_2023.csv"

# Colunas que vamos analisar
colunas = ['NU_INSCRICAO', 'TP_SEXO', 'SG_UF_PROVA', 'NU_NOTA_REDACAO']

# Carregando apenas as colunas necessárias
df = pd.read_csv(caminho, sep=';', low_memory=False, encoding='latin1')


# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Agrupa os dados por estado e gênero, calculando a média da nota de redação
media_estado_genero = df.groupby(['SG_UF_PROVA', 'TP_SEXO'])['NU_NOTA_REDACAO'].mean().unstack().sort_values(by='M', ascending=False)

# Exibe as médias
print("Média das notas de redação por estado e gênero (ordem decrescente para o gênero masculino):")
print(media_estado_genero)

# Criando um gráfico para visualizar as médias das notas de redação por estado e gênero
media_estado_genero.plot(kind='bar', figsize=(14, 8), width=0.8)

# Adicionando título e rótulos aos eixos
plt.title('Média das Notas de Redação por Estado e Gênero (ENEM 2023)', fontsize=16)
plt.xlabel('Estado', fontsize=12)
plt.ylabel('Média da Nota de Redação', fontsize=12)

# Exibindo o gráfico
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

