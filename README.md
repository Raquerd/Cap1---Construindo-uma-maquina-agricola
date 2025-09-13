# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# 🌾 FarmTech Solutions — Fase 4 

# **Construindo uma máquina agrícola**

## 👨‍🎓 Integrantes: 
- Lais Kurahashi
- Davi Ferreira
- Lucas Martinelli
  
## 👩‍🏫 Professores:
### Tutor(a) 
- Lucas Gomes Moreira
### Coordenador(a)
- André Godoi Chiovato

---

## 📜 Descrição

**💧 Sistema de Irrigação Inteligente com ESP32 + Análise Preditiva com Scikit-learn**

O projeto simula um sistema agrícola automatizado com o microcontrolador ESP32 na plataforma Wokwi, que monitora nutrientes do solo e realiza irrigação automática. Na Fase 4, foi incorporada uma camada de inteligência artificial com Scikit-learn para prever a necessidade de irrigação com base em dados históricos, além de um dashboard com Streamlit para visualização interativa e melhorias no banco de dados.

## 🚀 Objetivo 2.0

Monitorar e prever a necessidade de irrigação com base em dados do solo (umidade, pH, presença de fósforo e potássio), otimizando o uso de recursos hídricos na agricultura moderna.

---

## 🔮 Melhorias da Fase 4

- 🔍 **Modelagem preditiva com Scikit-learn:** algoritmo de classificação para prever quando irrigar com base em entradas simuladas.
- 🌐 **Integração com Streamlit:** interface web interativa com novos componentes, como filtros, visualizações e layout aprimorado.
- 📊 **Novo gráfico comparativo:** visualização da relação entre pH, umidade e necessidade de irrigação.
- 🧼 **Refatoração do código Python:** separação de funções, padronização, validação reforçada.
- 💾 **Banco de dados aprimorado:** campos melhor estruturados e normalização dos dados.
- 🖼️ **Serial Plotter (Wokwi):** atualização.

---

## 🧠 Sensores Simulados

- **Sensor de Fósforo (P):** Botão físico (TECLA 2)
  `Pressionado` → Fósforo presente 
  `Solto` → Fósforo ausente

- **Sensor de Potássio (K):** Botão físico (TECLA 1)
  `Pressionado` → Potássio presente  
  `Solto` → Potássio ausente

- **Sensor de pH:** Sensor LDR (luz como analogia ao valor de pH)  
  Variações na luminosidade simulam mudanças no pH do solo.

- **Sensor de Umidade:** Sensor DHT22  
  Mede a umidade relativa e simula a umidade do solo.

## ⚙️ Componentes Utilizados

- ESP32
- 2 Botões (P e K)
- LDR + Resistor
- Sensor DHT22
- Relé (representando a bomba)
- LED indicador da bomba
- Jumpers e resistores

## 🧪 Funcionamento (Fase 3)

- O sistema verifica os sensores a cada ciclo.
- Se **algum nutriente estiver ausente** ou a umidade for **inferior a 40%**, a irrigação é ativada.
- A **bomba funciona por 30 segundos** e depois desliga automaticamente.
- Mensagens são exibidas no monitor serial indicando o status do sistema.

## 🧪 Funcionamento 2.0

- Interface interativa:
- Simulador de irrigação -> com sugestões para a tomada de decisão
- Histórico
- Simulador de monitoramento em tempo real
- Previsão do tempo API
- Gráficos com insights e variações
- Decisões baseadas no modelo de ML
  
---

### 💬 Exemplo de Saída no Monitor Serial

Fósforo: Presente | Potássio: Presente | pH: 7.41 | Umidade: 88.5% -> Irrigação NÃO NECESSÁRIA

## 🖥️ Acesse o Projeto no Wokwi

🔗 [Clique aqui para ver no Wokwi](https://wokwi.com/projects/430519062599046145) 

## 🌿 Sistema de Irrigação Inteligente — FIAP
Este projeto simula um sistema de irrigação agrícola que utiliza sensores de umidade, pH, fósforo e potássio para tomar decisões automatizadas sobre o acionamento de uma bomba d’água. Os dados são armazenados em um banco de dados Oracle e podem ser visualizados em tempo real por um dashboard interativo.

---

## 📁 Estrutura do Projeto (fase 3)
|Arquivo   |	Descrição                                                                |
|:---------|:--------------------------------------------------------------------------|
|código.py |Script principal com menu interativo via terminal. Permite inserir, consultar, atualizar e excluir dados dos sensores, além de consultar API meteorológica.|
|dashboard.py|Dashboard interativo feito com Streamlit que exibe os dados armazenados no banco de forma gráfica (pH e umidade).|
|gerador de dados.py|	Simulador automático (comentado) para gerar e inserir dados falsos no banco Oracle com base em valores aleatórios.|
|rodar_dashboard.bat|	Atalho para abrir o dashboard com um clique no Windows (executa streamlit run dashboard.py).|

## 📁 Estrutura do Projeto 2.0
|Arquivo/Pasta   |	Descrição                                                                |
|:---------------|:--------------------------------------------------------------------------|
|pages |Menu de páginas da interface Streamlit.|
|1_Exploração_de_dados.py |Página Streamlit para explorar e filtrar dados de simulações do solo, com gráficos de umidade e pH.|
|2_Simulador_de_irrigação.py|	Simulador interativo que recomenda ligar ou desligar a bomba de irrigação com base em umidade, pH e nutrientes do solo, usando regras e modelo preditivo.|
|3_Histórico.py|	Página para visualizar, editar, salvar e baixar o histórico das simulações de irrigação.|
|4_Previsão_do_tempo.py|	Página que consulta e exibe a previsão do tempo para uma cidade, ajudando a decidir sobre a irrigação com base nas condições climáticas.|
|5_Insights.py|	Página com gráficos e estatísticas do histórico de decisões do modelo de irrigação.|
|6_Monitoramento_em_tempo_real.py|	Simula o monitoramento em tempo real de umidade, pH e nutrientes do solo para irrigação, atualizando os dados automaticamente a cada 2 segundos por 30 ciclos.|
|7_Gráficos_de_variação.py|	Página que mostra gráficos da umidade, pH e nutrientes (P e K) do solo ao longo do tempo, com insights básicos usando dados históricos.|
|Página_inicial.py|	Página inicial simples do Streamlit, apresentando o sistema de irrigação inteligente e seus principais recursos.|
|Modelo-preditivo.py|	Gera dados do solo, treina um modelo Random Forest para decidir quando ligar a bomba de irrigação e salva o modelo.|
|Sistema de Irrigação |	Conexão com Wokwi.|

---

## 🔧 Tecnologias Utilizadas
- Python 3.10.11
- Streamlit
- Oracle Database
- pandas
- matplotlib
- requests
- API pública: OpenWeather

## 🔧 Tecnologias Utilizadas 2.0
- Python 3.10.11
- Streamlit
- Oracle Database
- pandas
- matplotlib
- requests
- API pública: OpenWeather
- Altair
- joblib
- streamlit_autorefresh
- HTML

---

## 📦 Funcionalidades
✅ **código.py**
- Interface via terminal
- Integração com API meteorológica
- CRUD completo com banco Oracle
- Exportação dos dados para .xlsx
- Filtros por data
- Validação de campos

✅ **dashboard.py**
- Interface gráfica com Streamlit
- Tabela de dados em tempo real
- Gráficos:
- Umidade do solo
- pH do solo
- Filtro por mês digitado (a ser melhorado — usar st.selectbox() no futuro)

✅ **gerador de dados.py**
- bSimula a inserção automática de 100 registros com:
- Sensor P/K (binário)
- Umidade (10% a 80%)
- pH (4.5 a 8.0)
- Lógica de ativação da bomba


## 📦 Funcionalidades 2.0
✅ **1_Exploração_de_dados.py**
- Interface web para exploração de dados das simulações via Streamlit
- Carregamento do histórico salvo em CSV
- Filtros interativos para:
- Umidade do solo (slider)
- pH do solo (slider)
- Presença de fósforo (multiselect)
- Presença de potássio (multiselect)
- Exibição da tabela com dados filtrados em tempo real
- Gráficos tipo histograma para análise visual da distribuição:
- Umidade do solo
- pH do solo
- Textos explicativos simples sobre o significado dos gráficos para facilitar o entendimento
  
✅ **2_Simulador_de_irrigação.py**
- Interface Streamlit
- Entrada de dados do solo:
- Umidade (%)
- pH
- Presença de fósforo (P)
- Presença de potássio (K)
- Decisão sobre ligar ou desligar a bomba:
- Baseada em modelo de machine learning (Random Forest)
- Backup com regras manuais, caso o modelo falhe ou não esteja disponível
- Justificativas detalhadas e sugestões práticas com base nas condições do solo
- Armazenamento da simulação em um arquivo histórico (historico.csv)
- Feedback visual (mensagens de sucesso, aviso ou erro) sobre a recomendação feita

✅ **3_Histórico.py**
- Exibição interativa do histórico de simulações salvas (historico.csv)
- Permite editar diretamente os registros no Streamlit com o st.data_editor
- Botão para salvar alterações feitas na tabela
- Botão para limpar o histórico completo do arquivo
- Download do histórico no formato .csv

✅ **4_Previsão-do_tempo.py**
- Interface com o usuário para consulta de clima em tempo real
- Integração com a API pública OpenWeather
- Retorna dados como:
- Temperatura atual, mínima e máxima
- Umidade, pressão, visibilidade e vento
- Chuva na última hora, nascer e pôr do sol
- Condição geral do tempo (ex: "céu limpo", "chuva leve")
- Sugestão automática para irrigar ou não, com base nas condições climáticas
- Recurso para tratamento de erros caso a cidade informada esteja incorreta
  
✅ **5_Insights.py**
- Visualização de dados históricos registrados pelo sistema de irrigação
- Geração de gráficos interativos com o uso da biblioteca Altair
- Exibe:
- Total de simulações feitas
- Quantas vezes a bomba foi ligada/desligada
- Gráfico de decisões por mês
- Fornece análises estatísticas úteis:
- Média da umidade nas vezes em que a bomba foi ligada
- Média do pH nas vezes em que a bomba foi desligada
- Frequência da presença de fósforo (P) e potássio (K) nos solos analisados

✅ **5_Insights.py**
- Visualização de dados históricos registrados pelo sistema de irrigação
- Geração de gráficos interativos com o uso da biblioteca Altair
- Exibe:
- Total de simulações feitas
- Quantas vezes a bomba foi ligada/desligada
- Gráfico de decisões por mês
- Fornece análises estatísticas úteis:
- Média da umidade nas vezes em que a bomba foi ligada
- Média do pH nas vezes em que a bomba foi desligada
- Frequência da presença de fósforo (P) e potássio (K) nos solos analisados

✅ **6_Monitoramento_em_tempo_real.py**
- Simula a leitura em tempo real das condições do solo
- Atualiza automaticamente os dados a cada 2 segundos, por até 30 ciclos
- Mostra:
- Hora atual da leitura
- Umidade do solo (em %)
- pH do solo
- Presença ou ausência de fósforo (P) e potássio (K)
- Indicado para testes de visualização dinâmica do sistema

✅ **7_Gráficos_de_variação.py**
- Exibe gráficos temporais com os dados registrados no solo:
- Umidade (%)
- Presença de nutrientes (Fósforo e Potássio)
- Variação do pH
- Os gráficos são interativos, com tooltip exibindo a data e o valor
- Também exibe insights rápidos:
- Umidade e pH médios do solo
- Número de vezes em que P e K estiveram presentes

✅ **Página_inicial.py**
- Apresenta o propósito principal do sistema: auxiliar produtores a tomar decisões sobre irrigação com base em dados reais do solo.
- Explica o modelo de machine learning, que analisa:
- Presença de Fósforo (P)
- Presença de Potássio (K)
- pH do solo
- Umidade do solo

✅ **modelo-preditivo.py**
- Criar um modelo preditivo que decida se a bomba de irrigação deve ser ligada ou não, com base em:
- Umidade do solo
- pH
- Presença de Fósforo (P)
- Presença de Potássio (K)
- Geração de dados sintéticos
- Simula combinações variadas de umidade (10% a 100%), pH (4.5 a 9.0) e presença/ausência de P e K.
- Usa regras manuais para definir quando a bomba deveria ligar.
- Treinamento
- Separa os dados em treino e teste.
- Treina um modelo RandomForestClassifier.
- Avaliação
- Mostra acurácia e relatório de classificação.
- Exportação
- Salva o modelo como modelo_irrigacao.pkl para ser usado pelo sistema via Streamlit.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).
  

## 🔧 Como executar o código 

## 🚀 Como Executar
1. Instale os pacotes necessários
``` bash
pip install pandas oracledb matplotlib streamlit requests openpyxl

```
2. Execute o menu de operações
```bash
python código.py
```
3. Execute o dashboard
Com duplo clique, selecione rodar_dashboard.bat na pasta Scripts
Logo após a execução do arquivo.bat, será perguntado qual mês de consulta dos dados, basta inserir.
OBS: Os dados disponiveis no banco são apenas do mês 05

4. Simular dados automáticos
Descomente o código em gerador de dados.py e execute:
``` bash
python "gerador de dados.py"
```

