import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Pergunta 1")
# Carregar os dados diretamente dos arquivos CSV
dim_alimento_df = pd.read_csv("DimAlimento.csv")
fato_tabela_nutricional_df = pd.read_csv("FatoTabelaNutricional.csv")

merged_df = pd.merge(fato_tabela_nutricional_df, dim_alimento_df, left_on="Alimento_ID", right_on="ID")

# Configurar o estilo do Seaborn
sns.set(style="whitegrid")

# Plotar o boxplot da distribuição de gordura por tipo de alimento
plt.figure(figsize=(20, 10))
sns.boxplot(data=merged_df, x="TIPO_ALIMENTO", y="GORDURA_SATURADA", palette="Set3")

# Configurar o título e os rótulos dos eixos
plt.title("Distribuição de Gordura por Tipo de Alimento")
plt.xlabel("Tipo de Alimento")
plt.ylabel("Quantidade de Gordura")

# Rotacionar os rótulos do eixo x para melhor visualização
plt.xticks(rotation=45)

# Exibir o gráfico
st.pyplot(plt)

##############################################################################

# Carregar os dados diretamente dos arquivos CSV
dim_alimento_df = pd.read_csv("DimAlimento.csv")
fato_tabela_nutricional_df = pd.read_csv("FatoTabelaNutricional.csv")

merged_df = pd.merge(fato_tabela_nutricional_df, dim_alimento_df, left_on="Alimento_ID", right_on="ID")

# Agrupar por tipo de alimento e calcular as médias de gordura
grouped_df = merged_df.groupby("TIPO_ALIMENTO")["CARBOIDRATO"].mean()

# Configurar o estilo do Seaborn
sns.set(style="whitegrid")

# Plotar o gráfico de barras da média de gordura por tipo de alimento
plt.figure(figsize=(20, 10))
sns.barplot(data=grouped_df.reset_index(), x="TIPO_ALIMENTO", y="CARBOIDRATO", color="green")

# Configurar o título e os rótulos dos eixos
plt.title("Média de CARBOIDRATO por Tipo de Alimento")
plt.xlabel("Tipo de Alimento")
plt.ylabel("Média de CARBOIDRATO")

# Rotacionar os rótulos do eixo x para melhor visualização
plt.xticks(rotation=45)

# Exibir o gráfico
st.pyplot(plt)

################################################################################

# Carregar os dados diretamente dos arquivos CSV
dim_alimento_df = pd.read_csv("DimAlimento.csv")
fato_tabela_nutricional_df = pd.read_csv("FatoTabelaNutricional.csv")

merged_df = pd.merge(fato_tabela_nutricional_df, dim_alimento_df, left_on="Alimento_ID", right_on="ID")

# Agrupar por tipo de alimento e calcular as médias de gordura
grouped_df = merged_df.groupby("TIPO_ALIMENTO")["GORDURA_SATURADA"].mean()

# Configurar o estilo do Seaborn
sns.set(style="whitegrid")

# Plotar o gráfico de barras da média de gordura por tipo de alimento
plt.figure(figsize=(20, 10))
sns.barplot(data=grouped_df.reset_index(), x="TIPO_ALIMENTO", y="GORDURA_SATURADA", color="green")

# Configurar o título e os rótulos dos eixos
plt.title("Média de Gordura por Tipo de Alimento")
plt.xlabel("Tipo de Alimento")
plt.ylabel("Média de Gordura")

# Rotacionar os rótulos do eixo x para melhor visualização
plt.xticks(rotation=45)

# Exibir o gráfico
st.pyplot(plt)

###########################################################################################

# Carregar os dados diretamente dos arquivos CSV
dim_alimento_df = pd.read_csv("DimAlimento.csv")
fato_tabela_nutricional_df = pd.read_csv("FatoTabelaNutricional.csv")

merged_df = pd.merge(fato_tabela_nutricional_df, dim_alimento_df, left_on="Alimento_ID", right_on="ID")

# Agrupar por tipo de alimento e calcular as médias de proteína
grouped_df = merged_df.groupby("TIPO_ALIMENTO")["PROTEINA"].mean()

# Configurar o estilo do Seaborn
sns.set(style="whitegrid")

# Plotar o gráfico de barras da média de proteína por tipo de alimento
plt.figure(figsize=(20, 10))
sns.barplot(data=grouped_df.reset_index(), x="TIPO_ALIMENTO", y="PROTEINA", color="green")

# Configurar o título e os rótulos dos eixos
plt.title("Média de Proteína por Tipo de Alimento")
plt.xlabel("Tipo de Alimento")
plt.ylabel("Média de Proteína")

# Rotacionar os rótulos do eixo x para melhor visualização
plt.xticks(rotation=45)

# Exibir o gráfico
st.pyplot(plt)

################################################################################################
st.header("Pergunta 2")
# Carregar os dados dos arquivos CSV
dim_alimento_df = pd.read_csv('DimAlimento.csv')
fato_tabela_nutricional_df = pd.read_csv('FatoTabelaNutricional.csv')
dim_estabelecimento_df = pd.read_csv('DimEstabelecimento.csv')
dim_data_df = pd.read_csv('DimData.csv')

# Mesclar as tabelas DimAlimento, FatoTabelaNutricional, DimEstabelecimento e DimData
merged_df = pd.merge(fato_tabela_nutricional_df, dim_alimento_df, left_on="Alimento_ID", right_on="ID")
merged_df = pd.merge(merged_df, dim_estabelecimento_df, left_on="ESTABELECIMENTO_ID", right_on="ID")
merged_df = pd.merge(merged_df, dim_data_df, left_on="DATA_ID", right_on="DAY_ID")

# Configurar o estilo do Seaborn
sns.set(style="whitegrid")

# Criar um filtro para selecionar o tipo de alimento
tipos_alimentos = merged_df["TIPO_ALIMENTO"].unique()
selected_tipo_alimento = st.selectbox('Selecione o Tipo de Alimento', tipos_alimentos)

# Filtrar os dados de acordo com o tipo de alimento selecionado
filtered_df = merged_df[merged_df["TIPO_ALIMENTO"] == selected_tipo_alimento]

# Agrupar por ano e contar a quantidade total de ocorrências
grouped_df = filtered_df.groupby("YEAR")["TIPO_ALIMENTO"].count()

# Plotar o gráfico de barras da quantidade total de tipos de alimentos por ano
plt.figure(figsize=(20, 10))
sns.barplot(data=grouped_df.reset_index(), x="YEAR", y="TIPO_ALIMENTO", color="purple")

# Configurar o título e os rótulos dos eixos
plt.title(f"Quantidade Total de {selected_tipo_alimento} Consumidos por Ano")
plt.xlabel("Ano")
plt.ylabel(f"Quantidade Total de {selected_tipo_alimento}")

# Exibir o gráfico
st.pyplot(plt)

#######################################################################################################
st.header("Pergunta 3")
# Carregar os dados dos arquivos CSV
dim_alimento_df = pd.read_csv('DimAlimento.csv')
fato_tabela_nutricional_df = pd.read_csv('FatoTabelaNutricional.csv')
dim_estabelecimento_df = pd.read_csv('DimEstabelecimento.csv')
dim_data_df = pd.read_csv('DimData.csv')

# Filtrar a tabela DimAlimento pelo tipo de alimento selecionado
tipos_alimentos = dim_alimento_df['TIPO_ALIMENTO'].unique()
selected_tipo_alimento = st.selectbox('Selecione o Tipo de Alimento', tipos_alimentos[1:])

# Mesclar as tabelas DimAlimento, FatoTabelaNutricional, DimEstabelecimento e DimData
merged_df = pd.merge(fato_tabela_nutricional_df, dim_alimento_df, left_on="Alimento_ID", right_on="ID")
merged_df = pd.merge(merged_df, dim_estabelecimento_df, left_on="ESTABELECIMENTO_ID", right_on="ID")
merged_df = pd.merge(merged_df, dim_data_df, left_on="DATA_ID", right_on="DAY_ID")

# Filtrar os dados de acordo com o tipo de alimento selecionado
filtered_df = merged_df[merged_df["TIPO_ALIMENTO"] == selected_tipo_alimento]

# Agrupar por ano e tipo de estabelecimento e contar a quantidade total de ocorrências
grouped_df = filtered_df.groupby(["YEAR", "TIPO_ESTABELECIMENTO"])["TIPO_ALIMENTO"].count().reset_index()

# Plotar o gráfico de barras da quantidade total de tipos de alimentos por ano e tipo de estabelecimento
plt.figure(figsize=(20, 10))
sns.barplot(data=grouped_df, x="YEAR", y="TIPO_ALIMENTO", hue="TIPO_ESTABELECIMENTO", palette="Set2")

# Configurar o título e os rótulos dos eixos
plt.title(f"Quantidade Total de Alimentos do Tipo '{selected_tipo_alimento}' Consumidos por Ano e Tipo de Estabelecimento")
plt.xlabel("Ano")
plt.ylabel(f"Quantidade Total de Alimentos Consumidos")
plt.legend(title="Tipo de Estabelecimento")

# Exibir o gráfico
st.pyplot(plt)

#####################################################################################
st.header("Pergunta 4")
# Função para calcular as calorias de um alimento com base nas informações nutricionais
def calcular_calorias(row):
    calorias_carboidratos = row['CARBOIDRATO'] * 4  # 4 kcal por grama de carboidrato
    calorias_gordura = (row['GORDURA_SATURADA'] + row['GORDURA_INSATURADA']) * 9  # 9 kcal por grama de gordura
    calorias_proteina = row['PROTEINA'] * 4  # 4 kcal por grama de proteína
    return calorias_carboidratos + calorias_gordura + calorias_proteina

# Carregar os dados dos arquivos CSV
alimentos_df = pd.read_csv('DimAlimento.csv')
fato_tabela_nutricional_df = pd.read_csv('FatoTabelaNutricional.csv')

# Título do aplicativo
st.title("Calculadora de Calorias")

# Seleção de alimentos pelo cliente
alimentos_selecionados = st.multiselect("Selecione os alimentos:", alimentos_df['NOME'])

# Filtrar as informações nutricionais dos alimentos selecionados
nutricao_df = fato_tabela_nutricional_df[fato_tabela_nutricional_df['Alimento_ID'].isin(alimentos_df[alimentos_df['NOME'].isin(alimentos_selecionados)]['ID'])]
nutricao_df = nutricao_df[['Alimento_ID', 'CARBOIDRATO', 'GORDURA_SATURADA', 'GORDURA_INSATURADA', 'PROTEINA']]

# Calcular as calorias para os alimentos selecionados
nutricao_df['CALORIAS'] = nutricao_df.apply(calcular_calorias, axis=1)

# Calcular a quantidade total de calorias
total_calorias = nutricao_df['CALORIAS'].sum()

# Mapear os IDs dos alimentos para os nomes correspondentes
nutricao_df['NOME'] = nutricao_df['Alimento_ID'].map(dict(zip(alimentos_df['ID'], alimentos_df['NOME'])))

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(nutricao_df['NOME'], nutricao_df['CALORIAS'],width=0.3)
ax.set_xlabel('Alimento')
ax.set_ylabel('Calorias')
ax.set_title('Quantidade de Calorias por Alimento')
plt.xticks(rotation=45, ha='right')

# Adicionar barra de total de calorias
ax.bar("Total", total_calorias, color='orange', width=0.3)

# Exibir a quantidade total de calorias
st.write(f"Total de Calorias: {total_calorias} kcal")

st.pyplot(fig)
