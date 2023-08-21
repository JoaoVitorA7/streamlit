import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Função para calcular as calorias de um alimento com base nas informações nutricionais
def calcular_calorias(row):
    calorias_carboidratos = row['CARBOIDRATO'] * 4  # 4 kcal por grama de carboidrato
    calorias_gordura = (row['GORDURA_SATURADA'] + row['GORDURA_INSATURADA']) * 9  # 9 kcal por grama de gordura
    calorias_proteina = row['PROTEINA'] * 4  # 4 kcal por grama de proteína
    return calorias_carboidratos + calorias_gordura + calorias_proteina

# Conectar ao banco de dados MySQL
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="26112002",
    database="dw_lactosafe"
)

# Consultar a tabela DimAlimento para obter a lista de alimentos
query = "SELECT ID, NOME FROM DimAlimento"
alimentos_df = pd.read_sql(query, con=db_connection)

# Fechar a conexão com o banco de dados
db_connection.close()

# Título do aplicativo
st.title("Calculadora de Calorias")

# Seleção de alimentos pelo cliente
alimentos_selecionados = st.multiselect("Selecione os alimentos:", alimentos_df['NOME'])

# Consultar a tabela FatoTabelaNutricional para obter as informações nutricionais dos alimentos selecionados
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="26112002",
    database="dw_lactosafe"
)

query = f"SELECT Alimento_ID, CARBOIDRATO, GORDURA_SATURADA, GORDURA_INSATURADA, PROTEINA FROM FatoTabelaNutricional WHERE Alimento_ID IN ({','.join(map(str, alimentos_df[alimentos_df['NOME'].isin(alimentos_selecionados)]['ID']))})"
nutricao_df = pd.read_sql(query, con=db_connection)

# Calcular as calorias para os alimentos selecionados
nutricao_df['CALORIAS'] = nutricao_df.apply(calcular_calorias, axis=1)

# Calcular a quantidade total de calorias
total_calorias = nutricao_df['CALORIAS'].sum()

# Mapear os IDs dos alimentos para os nomes correspondentes
nutricao_df['NOME'] = nutricao_df['Alimento_ID'].map(dict(zip(alimentos_df['ID'], alimentos_df['NOME'])))

# Fechar a conexão com o banco de dados
db_connection.close()

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
