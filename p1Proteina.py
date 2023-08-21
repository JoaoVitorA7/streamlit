import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

# Conectar ao banco de dados MySQL
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="26112002",
    database="dw_lactosafe"
)

# Carregar os dados diretamente da tabela DimAlimento e FatoTabelaNutricional
dim_alimento_query = "SELECT * FROM DimAlimento"
fato_tabela_nutricional_query = "SELECT * FROM FatoTabelaNutricional"

dim_alimento_df = pd.read_sql(dim_alimento_query, con=db_connection)
fato_tabela_nutricional_df = pd.read_sql(fato_tabela_nutricional_query, con=db_connection)

# Fechar a conexão com o banco de dados
db_connection.close()

merged_df = pd.merge(fato_tabela_nutricional_df, dim_alimento_df, left_on="Alimento_ID", right_on="ID")

# Agrupar por tipo de alimento e calcular as médias de gordura
grouped_df = merged_df.groupby("TIPO_ALIMENTO")["PROTEINA"].mean()

# Configurar o estilo do Seaborn
sns.set(style="whitegrid")

# Plotar o gráfico de barras da média de gordura por tipo de alimento
plt.figure(figsize=(20, 10))
sns.barplot(data=grouped_df.reset_index(), x="TIPO_ALIMENTO", y="PROTEINA", color="green")

# Configurar o título e os rótulos dos eixos
plt.title("Média de Proteina por Tipo de Alimento")
plt.xlabel("Tipo de Alimento")
plt.ylabel("Média de Proteina")

# Rotacionar os rótulos do eixo x para melhor visualização
plt.xticks(rotation=45)

# Exibir o gráfico
st.pyplot(plt)
