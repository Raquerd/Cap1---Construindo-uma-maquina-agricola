import streamlit as st
import pandas as pd
import altair as alt
import os

st.title("Insights do Modelo de Irrigação")

HIST_PATH = "historico.csv"

if not os.path.exists(HIST_PATH):
    st.warning("Nenhum dado histórico encontrado para gerar insights.")
    st.stop()

# Carrega dados
df = pd.read_csv(HIST_PATH, sep=',')
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True, errors='coerce')


# Quantidade total de simulações
total_simulacoes = len(df)
st.markdown(f"**Total de simulações registradas:** {total_simulacoes}")

# Quantidade de decisões de ligar e desligar
ligar_count = (df['Decisão'] == "Ligar a bomba de irrigação").sum()
desligar_count = (df['Decisão'] == "Desligar a bomba de irrigação").sum()

col1, col2 = st.columns(2)
col1.metric("Bomba ligada", ligar_count)
col2.metric("Bomba desligada", desligar_count)

# Gráfico de decisões ao longo do tempo (por mês)
df['Mês'] = df['Data'].dt.to_period('M').dt.to_timestamp()

grafico_decisoes = alt.Chart(df).mark_bar().encode(
    x=alt.X('Mês:T', title='Mês'),
    y=alt.Y('count()', title='Número de decisões'),
    color='Decisão',
    tooltip=['Mês', 'Decisão', 'count()']
).properties(
    width=700,
    height=400,
    title='Decisões da bomba de irrigação por mês'
)

st.altair_chart(grafico_decisoes, use_container_width=True)

# Insights adicionais baseados no histórico
st.header("Análises adicionais")

# Média da umidade em simulações que ligaram a bomba
media_umidade_ligar = df.loc[df['Decisão'] == "Ligar a bomba de irrigação", 'Umidade (%)'].mean()
st.write(f"- Média da umidade do solo quando a bomba foi ligada: **{media_umidade_ligar:.2f}%**")

# Média do pH em simulações que desligaram a bomba
media_ph_desligar = df.loc[df['Decisão'] == "Desligar a bomba de irrigação", 'pH'].mean()
st.write(f"- Média do pH do solo quando a bomba foi desligada: **{media_ph_desligar:.2f}**")

# Frequência de presença de fósforo e potássio
freq_p = df['P'].value_counts(normalize=True).mul(100).round(2)
freq_k = df['K'].value_counts(normalize=True).mul(100).round(2)

st.write(f"- Frequência de presença de fósforo (P):\n  - Presente: {freq_p.get('Presente', 0)}%\n  - Ausente: {freq_p.get('Ausente', 0)}%")
st.write(f"- Frequência de presença de potássio (K):\n  - Presente: {freq_k.get('Presente', 0)}%\n  - Ausente: {freq_k.get('Ausente', 0)}%")
