import streamlit as st
import pandas as pd
import datetime
import os
import joblib

st.title("Simulador de Irrigação")
st.markdown("""
Este simulador ajuda a tomar decisões sobre quando ligar ou desligar a bomba de irrigação com base em condições do solo, como umidade, pH e presença de nutrientes essenciais.
""")

# Entradas do usuário
umidade_percentual = st.slider("Umidade do solo (%)", 0, 100, 50)
ph = st.slider("pH do solo", 3.0, 9.0, 6.5, 0.1)
p = st.radio("Fósforo (P) presente?", ["Presente", "Ausente"], horizontal=True)
k = st.radio("Potássio (K) presente?", ["Presente", "Ausente"], horizontal=True)

# Converte Presente/Ausente para binário
p_bin = 1 if p == "Presente" else 0
k_bin = 1 if k == "Presente" else 0

# Carrega Modelo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # scripts/pages/
modelo_path = os.path.abspath(os.path.join(BASE_DIR, "..", "modelo_irrigacao.pkl"))
model = None
if os.path.exists(modelo_path):
    model = joblib.load(modelo_path)
else:
    st.warning("Modelo preditivo não encontrado. As decisões serão baseadas em regras.")

# Função com explicações e sugestões
def avaliar(umidade: int, ph_val: float, p_flag: int, k_flag: int):
    relatorio = []
    feedback = []
    sugestoes = []

    if umidade < 20:
        relatorio.append("Umidade crítica (<20%) — solo muito seco")
        feedback.append("Necessita irrigação urgente")
    elif umidade < 40:
        relatorio.append("Umidade baixa (<40%)")
        feedback.append("Irrigação recomendada")
    elif umidade > 80:
        relatorio.append("Umidade alta (>80%) — solo saturado")
        feedback.append("Evitar irrigação")
    else:
        relatorio.append("Umidade ideal (40‑80%)")
        feedback.append("Sem necessidade urgente")

    if ph_val < 5.5:
        relatorio.append("pH ácido (<5.5)")
        feedback.append("Atenção ao pH ácido")
        sugestoes.append("Aplicar calcário para corrigir acidez.")
    elif ph_val > 8.0:
        relatorio.append("pH alcalino (>8.0)")
        feedback.append("Atenção ao pH alcalino")
        sugestoes.append("Aplicar enxofre ou matéria orgânica para corrigir alcalinidade.")
    else:
        relatorio.append("pH ideal (5.5‑8.0)")

    if (p_flag, k_flag) == (0, 0):
        feedback.append("Fósforo e Potássio ausentes")
        sugestoes.append("Aplicar adubos ricos em fósforo (P) e potássio (K).")
    elif (p_flag, k_flag) == (0, 1):
        feedback.append("Fósforo ausente")
        sugestoes.append("Aplicar fertilizantes com fósforo, como superfosfato.")
    elif (p_flag, k_flag) == (1, 0):
        feedback.append("Potássio ausente")
        sugestoes.append("Aplicar fertilizantes com potássio, como cloreto de potássio.")
    else:
        feedback.append("P e K presentes")

    # Decisão final baseada em regras simples
    if umidade < 40:
        decisao = "Ligar a bomba de irrigação"
    elif umidade > 80:
        decisao = "Desligar a bomba de irrigação"
    else:
        if ph_val < 5.5 or ph_val > 8.0:
            decisao = "Ligar a bomba de irrigação"
        else:
            decisao = "Desligar a bomba de irrigação"

    return decisao, relatorio, feedback, sugestoes

# Executa quando clicar no botão
if st.button("Gerar recomendação"):

    decisao = None
    if model:
        try:
            pred = model.predict([[p_bin, k_bin, ph, umidade_percentual]])[0]
            decisao_ml = "Ligar a bomba de irrigação" if pred == 1 else "Desligar a bomba de irrigação"

            if pred == 1:
                st.success("Decisão tomada automaticamente pelo modelo preditivo: **Ligar a bomba de irrigação**.")
            else:
                st.info("Decisão tomada automaticamente pelo modelo preditivo: **Desligar a bomba de irrigação**.")

            decisao = decisao_ml

        except Exception as e:
            st.error(f"Erro na predição do modelo: {e}")
            st.info("Decisão baseada em regras foi aplicada por segurança.")

    # Avaliação com regras
    decisao_regra, relatorio, feedback, sugestoes = avaliar(umidade_percentual, ph, p_bin, k_bin)

    # Se não teve decisão do modelo, usar a da regra
    if decisao is None:
        decisao = decisao_regra
        st.info("Decisão tomada com base em regras.")

    # Exibe decisão final
    st.subheader("Decisão final")
    if "Desligar" in decisao:
        st.error(decisao)
    else:
        st.success(decisao)

    # Mostra relatório, feedback e sugestões sempre
    just_texto = "*Relatório:*\n- " + "\n- ".join(relatorio)
    just_texto += "\n\n*Feedback:*\n- " + "\n- ".join(feedback)
    if sugestoes:
        just_texto += "\n\n*Sugestões:*\n- " + "\n- ".join(sugestoes)

    st.markdown(just_texto)

    # Salvar histórico
    data_reg = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    novo = pd.DataFrame({
        "Data": [data_reg],
        "Umidade (%)": [umidade_percentual],
        "pH": [ph],
        "P": [p],
        "K": [k],
        "Decisão": [decisao],
        "Justificativa": [just_texto.replace("\n", " ")]
    })

    if os.path.exists("historico.csv"):
        historico = pd.read_csv("historico.csv")
        pd.concat([historico, novo], ignore_index=True).to_csv("historico.csv", index=False, encoding="utf-8-sig")
    else:
        novo.to_csv("historico.csv", index=False, encoding="utf-8-sig")

    st.success("Decisão salva no histórico.")
