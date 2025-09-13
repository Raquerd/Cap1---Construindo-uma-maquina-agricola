import streamlit as st
import pandas as pd
import altair as alt

HIST_PATH = "historico.csv"

# Lê CSV 
df = pd.read_csv(HIST_PATH)

# Converte Data para datetime
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True, errors='coerce')

# Cria coluna Mês (agrupamento)
df['Mês'] = df['Data'].dt.to_period('M').dt.to_timestamp()

st.title("Gráficos de Variação do Solo")

# Gráfico de Umidade do solo ao longo do tempo
umidade_chart = alt.Chart(df).mark_line(point=True).encode(
    x='Data',
    y=alt.Y('Umidade (%)', title='Umidade (%)'),
    tooltip=['Data', 'Umidade (%)']
).properties(title="Variação da Umidade do Solo")

st.altair_chart(umidade_chart, use_container_width=True)

# Prepara dados para nutrientes - binários
df_nutrientes = df.melt(
    id_vars=['Data'], 
    value_vars=['P', 'K'], 
    var_name='Nutriente', 
    value_name='Presença'
)

# Filtra só quando presença = 1
df_nutrientes = df_nutrientes[df_nutrientes['Presença'] == 1]

nutrientes_chart = alt.Chart(df_nutrientes).mark_point(filled=True, size=100).encode(
    x='Data',
    y='Nutriente',
    tooltip=['Data', 'Nutriente']
).properties(title="Presença de Nutrientes (P e K) no Solo")

st.altair_chart(nutrientes_chart, use_container_width=True)

# Gráfico de pH ao longo do tempo
ph_chart = alt.Chart(df).mark_line(color='green', point=True).encode(
    x='Data',
    y=alt.Y('pH', title='pH do Solo'),
    tooltip=['Data', 'pH']
).properties(title="Variação do pH do Solo")

st.altair_chart(ph_chart, use_container_width=True)

# Insights simples
st.subheader("Insights")
umidade_media = df['Umidade (%)'].mean()
ph_medio = df['pH'].mean()
st.write(f"- Umidade média do solo: {umidade_media:.2f}%")
st.write(f"- pH médio do solo: {ph_medio:.2f}")

# Converte 'P' e 'K' para valores binários
df['P_bin'] = df['P'].map({'Presente': 1, 'Ausente': 0})
df['K_bin'] = df['K'].map({'Presente': 1, 'Ausente': 0})

# Soma presença de nutrientes
p_presenca = df['P_bin'].sum()
k_presenca = df['K_bin'].sum()

# Total de registros
total = len(df)

# Mostra no Streamlit
st.markdown("### Presença de Nutrientes")
st.write(f"Fósforo presente em **{p_presenca}** de {total} simulações ({(p_presenca/total)*100:.1f}%)")
st.write(f"Potássio presente em **{k_presenca}** de {total} simulações ({(k_presenca/total)*100:.1f}%)")
