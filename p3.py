import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar ao banco de dados MySQL
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="26112002",
    database="dw_lactosafe"
)

# Executar a consulta para obter a lista de tipos de alimentos
tipos_alimentos_query = "SELECT DISTINCT TIPO_ALIMENTO FROM DimAlimento"
tipos_alimentos = pd.read_sql(tipos_alimentos_query, con=db_connection)["TIPO_ALIMENTO"].tolist()

# Fechar a conexão com o banco de dados
db_connection.close()

# Criar um filtro para selecionar o tipo de alimento
selected_tipo_alimento = st.selectbox('Selecione o Tipo de Alimento', tipos_alimentos)

# Conectar novamente ao banco de dados
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="26112002",
    database="dw_lactosafe"
)

# Executar a consulta para obter os dados do gráfico para MERCADO
query_mercado = f"""
    SELECT YEAR(d.DAY_DATE) AS Ano, COUNT(*) AS QuantidadeTotal
    FROM FatoTabelaNutricional fn
    JOIN DimData d ON fn.DATA_ID = d.DAY_ID
    JOIN DimEstabelecimento de ON fn.ESTABELECIMENTO_ID = de.ID
    JOIN DimAlimento da ON fn.Alimento_ID = da.ID
    WHERE YEAR(d.DAY_DATE) >= (SELECT MIN(YEAR(DAY_DATE)) FROM FatoTabelaNutricional)
    AND da.TIPO_ALIMENTO = '{selected_tipo_alimento}'
    AND de.TIPO_ESTABELECIMENTO = 'MERCADO'
    GROUP BY Ano
    ORDER BY Ano
"""

# Executar a consulta para obter os dados do gráfico para RESTAURANTE
query_restaurante = f"""
    SELECT YEAR(d.DAY_DATE) AS Ano, COUNT(*) AS QuantidadeTotal
    FROM FatoTabelaNutricional fn
    JOIN DimData d ON fn.DATA_ID = d.DAY_ID
    JOIN DimEstabelecimento de ON fn.ESTABELECIMENTO_ID = de.ID
    JOIN DimAlimento da ON fn.Alimento_ID = da.ID
    WHERE YEAR(d.DAY_DATE) >= (SELECT MIN(YEAR(DAY_DATE)) FROM FatoTabelaNutricional)
    AND da.TIPO_ALIMENTO = '{selected_tipo_alimento}'
    AND de.TIPO_ESTABELECIMENTO = 'RESTAURANTE'
    GROUP BY Ano
    ORDER BY Ano
"""

data_mercado = pd.read_sql(query_mercado, con=db_connection)
data_restaurante = pd.read_sql(query_restaurante, con=db_connection)

# Fechar a conexão com o banco de dados
db_connection.close()

# Juntar os dados de mercado e restaurante para o mesmo DataFrame
data_merged = pd.merge(data_mercado, data_restaurante, on="Ano", how="outer", suffixes=('_Mercado', '_Restaurante'))
data_merged.fillna(0, inplace=True)

# Criar o gráfico usando o Streamlit
st.title(f"Quantidade Total de Alimentos do Tipo '{selected_tipo_alimento}' Consumidos por Ano")
fig, ax = plt.subplots(figsize=(10, 6))
data_merged.plot(kind="bar", x="Ano", ax=ax)
ax.set_xlabel("Ano")
ax.set_ylabel("Quantidade Total de Alimentos Consumidos")
ax.set_title(f"Quantidade Total de Alimentos do Tipo '{selected_tipo_alimento}' Consumidos por Ano")
ax.legend(["Mercado", "Restaurante"])
st.pyplot(fig)
