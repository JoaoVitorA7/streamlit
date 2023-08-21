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

# Criar um filtro para selecionar o tipo de estabelecimento (Mercado ou Restaurante)
selected_tipo_estabelecimento = st.selectbox('Selecione o Tipo de Estabelecimento', ['MERCADO', 'RESTAURANTE'])

# Conectar novamente ao banco de dados
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="26112002",
    database="dw_lactosafe"
)

# Obter o ano mínimo da tabela DimData
query_min_year = "SELECT MIN(YEAR(DAY_DATE)) FROM FatoTabelaNutricional"
result = pd.read_sql(query_min_year, con=db_connection)
min_year = result.iloc[0, 0]

# Executar a consulta para obter os dados do gráfico para MERCADO
query_mercado = f"""
    SELECT YEAR(d.DAY_DATE) AS Ano, da.TIPO_ALIMENTO, COUNT(*) AS QuantidadeTotal
    FROM FatoTabelaNutricional fn
    JOIN DimData d ON fn.DATA_ID = d.DAY_ID
    JOIN DimAlimento da ON fn.Alimento_ID = da.ID
    JOIN DimEstabelecimento de ON fn.ESTABELECIMENTO_ID = de.ID
    WHERE YEAR(d.DAY_DATE) >= {min_year} AND da.TIPO_ALIMENTO = '{selected_tipo_alimento}' AND de.TIPO_ESTABELECIMENTO = '{selected_tipo_estabelecimento}'
    GROUP BY Ano, da.TIPO_ALIMENTO
    ORDER BY Ano
"""

data_mercado = pd.read_sql(query_mercado, con=db_connection)

# Fechar a conexão com o banco de dados
db_connection.close()

# Criar um mapeamento de cores para os tipos de alimentos
tipo_alimento_unique = data_mercado["TIPO_ALIMENTO"].unique()
tipo_alimento_color_map = sns.color_palette("Set2", n_colors=len(tipo_alimento_unique))
tipo_alimento_color_dict = {tipo: tipo_alimento_color_map[i] for i, tipo in enumerate(tipo_alimento_unique)}

# Criar o gráfico usando o Streamlit
st.title("Quantidade Total de Alimentos Consumidos por Tipo ao Longo dos Anos")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=data_mercado, x="Ano", y="QuantidadeTotal", hue="TIPO_ALIMENTO", palette=tipo_alimento_color_dict)
ax.set_xlabel("Ano")
ax.set_ylabel("Quantidade Total de Alimentos Consumidos")
ax.set_title(f"Quantidade Total de Alimentos Consumidos por Tipo ao Longo dos Anos - Tipo: {selected_tipo_alimento}")
st.pyplot(fig)
