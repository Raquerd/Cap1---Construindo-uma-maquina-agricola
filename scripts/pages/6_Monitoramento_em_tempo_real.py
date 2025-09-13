import streamlit as st
import random
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# Atualiza a cada 2 segundos, até 30 vezes
count = st_autorefresh(interval=2000, limit=30, key="monitor")

st.title("Monitoramento em Tempo Real da Irrigação")
st.markdown("Dados atualizados automaticamente a cada 2 segundos.")

umidade_atual = random.uniform(10, 90)
ph_atual = random.uniform(4.5, 8.5)
p_atual = random.choice([0, 1])
k_atual = random.choice([0, 1])

st.write(f"**Hora da leitura:** {datetime.now().strftime('%H:%M:%S')}")
st.write(f"Umidade do solo: **{umidade_atual:.1f}%**")
st.write(f"pH do solo: **{ph_atual:.2f}**")
st.write(f"Fósforo (P) presente: **{'Sim' if p_atual else 'Não'}**")
st.write(f"Potássio (K) presente: **{'Sim' if k_atual else 'Não'}**")

if count == 30:
    st.write("Fim da simulação.")
