import streamlit as st

st.set_page_config(page_title="Sistema de Irrigação Inteligente", page_icon="💧", layout="centered")

st.markdown("<h1 style='text-align: center; color: white ;'>💧 Bem-vindo(a) ao Sistema de Irrigação Inteligente</h1>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
<p style="font-size:18px; text-align: center; color: white;">
Este aplicativo usa um <b>modelo de machine learning</b> para ajudar produtores rurais a saber <b>quando ligar ou desligar a bomba de irrigação</b>.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div style="max-width: 600px; margin: auto; font-size: 16px; color: white; line-height: 1.5;">
    <p>Ele analisa os principais parâmetros do solo para fornecer uma sugestão automática e justificada:</p>
    <ul>
        <li><b>Fósforo (P)</b></li>
        <li><b>Potássio (K)</b></li>
        <li><b>pH do solo</b></li>
        <li><b>Umidade</b></li>
    </ul>
    <p>Com base nesses dados, o sistema ajuda a garantir que sua plantação receba a irrigação adequada, economizando recursos e promovendo a saúde do solo.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

