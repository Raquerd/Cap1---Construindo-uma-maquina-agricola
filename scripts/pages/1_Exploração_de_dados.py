import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="Exploração de Dados", page_icon="📊")

st.title("Exploração de Dados")
st.markdown("""
Nesta página você pode visualizar e analisar os dados das simulações feitas no sistema.

Aqui é possível entender as características do solo registradas, como:
- Umidade (%)
- pH
- Presença de nutrientes (Fósforo e Potássio)

Use as ferramentas abaixo para filtrar e explorar os dados facilmente.
""")

# Caminho para histórico
HIST_PATH = "historico.csv"

if not os.path.exists(HIST_PATH):
    st.info("Nenhum dado encontrado. Faça uma simulação primeiro.")
    st.stop()

# Carrega dados
df = pd.read_csv(HIST_PATH)

# Filtros simples para explorar os dados

st.subheader("Filtrar Dados")

umidade_min, umidade_max = st.slider(
    "Filtrar por umidade (%)",
    min_value=0,
    max_value=100,
    value=(int(df["Umidade (%)"].min()), int(df["Umidade (%)"].max()))
)

ph_min, ph_max = st.slider(
    "Filtrar por pH",
    min_value=3.0,
    max_value=9.0,
    value=(float(df["pH"].min()), float(df["pH"].max())),
    step=0.1
)

p_filter = st.multiselect(
    "Fósforo (P)",
    options=df["P"].unique(),
    default=list(df["P"].unique())
)

k_filter = st.multiselect(
    "Potássio (K)",
    options=df["K"].unique(),
    default=list(df["K"].unique())
)

# Aplica filtro
df_filtrado = df[
    (df["Umidade (%)"] >= umidade_min) &
    (df["Umidade (%)"] <= umidade_max) &
    (df["pH"] >= ph_min) &
    (df["pH"] <= ph_max) &
    (df["P"].isin(p_filter)) &
    (df["K"].isin(k_filter))
]

st.subheader("Dados Filtrados")
st.dataframe(df_filtrado, use_container_width=True)

# Gráficos simples para visualização

col1, col2 = st.columns(2)

with col1:
    st.subheader("Umidade do Solo (%)")

    fig_umid, ax1 = plt.subplots()
    ax1.hist(df["Umidade (%)"], bins=10, color='skyblue', edgecolor='black')
    ax1.set_xlabel("Umidade (%)")
    ax1.set_ylabel("Frequência")
    ax1.set_title("Histograma de Umidade")
    st.pyplot(fig_umid)

    st.markdown("""
    **O que significa?**

    - Barras mais altas mostram umidade mais comum.
    - Esquerda: solo seco.
    - Meio: umidade boa.
    - Direita: solo muito molhado.
    """)

with col2:
    st.subheader("pH do Solo")

    fig_ph, ax2 = plt.subplots()
    ax2.hist(df["pH"], bins=10, color='lightgreen', edgecolor='black')
    ax2.set_xlabel("pH")
    ax2.set_ylabel("Frequência")
    ax2.set_title("Histograma de pH")
    st.pyplot(fig_ph)

    st.markdown("""
    **O que significa?**

    - Barras altas mostram pH mais frequente.
    - < 5.5: solo ácido (menos ideal).
    - 5.5 - 8.0: solo ideal.
    - (> 8.0): solo alcalino (menos ideal).
    """)