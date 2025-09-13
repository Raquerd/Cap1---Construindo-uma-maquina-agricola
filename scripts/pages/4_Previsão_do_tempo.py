import streamlit as st
import requests
from datetime import datetime

API_KEY = '7621dd8760f87d562a4e5a21bffbdc36'

def pegar_dados_tempo(cidade):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br'
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        st.error("Erro ao buscar dados da API. Verifique o nome da cidade.")
        return None

def formatar_hora(timestamp, timezone):
    # Ajusta o timestamp com o timezone da cidade e formata como HH:MM
    dt = datetime.utcfromtimestamp(timestamp + timezone)
    return dt.strftime('%H:%M')

def mostrar_dados(dados):
    st.subheader(f"Previsão do tempo para {dados['name']}, {dados['sys']['country']}")

    temp = dados['main']['temp']
    temp_min = dados['main']['temp_min']
    temp_max = dados['main']['temp_max']
    umidade = dados['main']['humidity']
    pressao = dados['main']['pressure']
    vento = dados['wind']['speed']
    visibilidade = dados.get('visibility', 0) / 1000  # em km
    condicao = dados['weather'][0]['description'].capitalize()
    chuva_1h = dados.get('rain', {}).get('1h', 0)
    nascer_sol = formatar_hora(dados['sys']['sunrise'], dados['timezone'])
    por_sol = formatar_hora(dados['sys']['sunset'], dados['timezone'])

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Temperatura:** {temp} °C")
        st.write(f"Temperatura mínima: {temp_min} °C")
        st.write(f"Temperatura máxima: {temp_max} °C")
        st.write(f"Umidade do ar: {umidade} %")
        st.write(f"Pressão atmosférica: {pressao} hPa")

    with col2:
        st.write(f"**Velocidade do vento:** {vento} m/s")
        st.write(f"Visibilidade: {visibilidade:.1f} km")
        st.write(f"Condição: {condicao}")
        st.write(f"Chuva na última hora: {chuva_1h} mm")
        st.write(f"Nascer do sol: {nascer_sol}")
        st.write(f"Pôr do sol: {por_sol}")

    # Sugestão para irrigação 
    sugestao = ""
    if chuva_1h > 0:
        sugestao = "Não irrigar — houve chuva recente."
    elif umidade < 40:
        sugestao = "Irrigar — umidade do ar está baixa."
    elif temp > 30:
        sugestao = "Irrigar — temperatura alta."
    else:
        sugestao = "Monitorar — condições estão boas."

    st.markdown("---")
    st.markdown("**Sugestão:**")
    st.write(sugestao)

# Interface 
st.title("Previsão do Tempo para Irrigação")
cidade = st.text_input("Digite o nome da cidade:", "São Paulo")

if cidade:
    dados_tempo = pegar_dados_tempo(cidade)
    if dados_tempo:
        mostrar_dados(dados_tempo)
