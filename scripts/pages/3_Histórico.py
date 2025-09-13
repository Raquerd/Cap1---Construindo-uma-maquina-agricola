import streamlit as st
import pandas as pd
from io import StringIO
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.header("Histórico de Simulações")
HIST_PATH = "historico.csv"

if not os.path.exists(HIST_PATH):
    st.info("Nenhum histórico salvo ainda.")
    st.stop()

df = pd.read_csv(HIST_PATH, sep=';')

# Data salvamento
edited_df = st.data_editor(
    df,
    num_rows="dynamic",
    key="hist_edit"
)

col1, col2, _ = st.columns(3)

with col1:
    if st.button("Salvar alterações"):
        edited = st.session_state["hist_edit"]["edited_rows"]
        if edited:
            df.update(pd.DataFrame.from_dict(edited, orient="index"))
        df.to_csv(HIST_PATH, index=False, encoding='utf-8-sig', sep=';')
        st.success("Histórico salvo.")

with col2:
    if st.button("Limpar histórico"):
        if os.path.exists(HIST_PATH):
            os.remove(HIST_PATH)
            st.warning("Histórico apagado. Para confirmar, por favor clique novamente no botão 'Limpar histórico' para atualizar a tela.")
        else:
            st.info("Histórico já estava limpo.")

# Download CSV
csv = df.to_csv(index=False, encoding='utf-8-sig', sep=';').encode('utf-8-sig')
st.download_button(
    "Baixar CSV",
    csv,
    "historico.csv",
    "text/csv"
)
