# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto
**Construindo uma maquina agricola**
## Nome do grupo

## 👨‍🎓 Integrantes: 
- Lais Kurahashi
- Davi Ferreira
- Lucas Martinelli 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 4</a> 

## 👩‍🏫 Professores:
### Tutor(a) 
- Lucas Gomes Moreira
### Coordenador(a)
- André Godoi Chiovato


## 📜 Descrição

# 💧 Sistema de Irrigação Inteligente com ESP32 - Simulação Wokwi

Este projeto simula um sistema agrícola automatizado usando um microcontrolador ESP32 na plataforma [Wokwi](https://wokwi.com/). A irrigação é controlada com base na presença de nutrientes (Fósforo e Potássio), no pH e na umidade do solo. Quando detectadas condições inadequadas, a bomba é ativada automaticamente por 30 segundos.

## 🚀 Objetivo

Monitorar as condições do solo e realizar irrigação automática somente quando necessário, otimizando o uso de recursos hídricos na agricultura.

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

## 🧪 Funcionamento

- O sistema verifica os sensores a cada ciclo.
- Se **algum nutriente estiver ausente** ou a umidade for **inferior a 40%**, a irrigação é ativada.
- A **bomba funciona por 30 segundos** e depois desliga automaticamente.
- Mensagens são exibidas no monitor serial indicando o status do sistema.

### 💬 Exemplo de Saída no Monitor Serial

Fósforo: Presente | Potássio: Presente | pH: 7.41 | Umidade: 88.5% -> Irrigação NÃO NECESSÁRIA

## 🖥️ Acesse o Projeto no Wokwi

🔗 [Clique aqui para ver no Wokwi](https://wokwi.com/projects/430519062599046145) 

___
## 🌿 Sistema de Irrigação Inteligente — FIAP
Este projeto simula um sistema de irrigação agrícola que utiliza sensores de umidade, pH, fósforo e potássio para tomar decisões automatizadas sobre o acionamento de uma bomba d’água. Os dados são armazenados em um banco de dados Oracle e podem ser visualizados em tempo real por um dashboard interativo.

## 📁 Estrutura do Projeto
|Arquivo   |	Descrição                                                                |
|:---------|:--------------------------------------------------------------------------|
|código.py |Script principal com menu interativo via terminal. Permite inserir, consultar, atualizar e excluir dados dos sensores, além de consultar API meteorológica.|
|dashboard.py|Dashboard interativo feito com Streamlit que exibe os dados armazenados no banco de forma gráfica (pH e umidade).|
|gerador de dados.py|	Simulador automático (comentado) para gerar e inserir dados falsos no banco Oracle com base em valores aleatórios.|
|rodar_dashboard.bat|	Atalho para abrir o dashboard com um clique no Windows (executa streamlit run dashboard.py).|

## 🔧 Tecnologias Utilizadas
- Python 3.10.11
- Streamlit
- Oracle Database
- pandas
- matplotlib
- requests
- API pública: OpenWeather

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

