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
