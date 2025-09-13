import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

# 1. Gera dataset sintético
def gerar_dataset_simples():
    data = []
    for umidade in range(10, 101, 10):  # 10 a 100%
        for ph in [4.5, 5.5, 6.5, 7.5, 8.5, 9.0]:  # valores variados pH
            for p_flag in [0, 1]:
                for k_flag in [0, 1]:
                    # Regras para ligar bomba
                    if umidade < 20:
                        ligar = 1
                    elif umidade < 40:
                        ligar = 1
                    elif 40 <= umidade <= 80:
                        if ph < 5.5 or ph > 8.0:
                            ligar = 1
                        elif p_flag == 0 or k_flag == 0:
                            ligar = 1
                        else:
                            ligar = 0
                    else:
                        ligar = 0
                    
                    data.append({
                        "umidade": umidade,
                        "ph": ph,
                        "p_present": p_flag,
                        "k_present": k_flag,
                        "ligar_bomba": ligar
                    })
    df = pd.DataFrame(data)
    return df

# Gera dados
df = gerar_dataset_simples()

# Separa features e target
X = df[["p_present", "k_present", "ph", "umidade"]]
y = df["ligar_bomba"]

# Treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Avaliar modelo
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Salvar modelo
joblib.dump(model, "modelo_irrigacao.pkl")
print("Modelo salvo em 'modelo_irrigacao.pkl'")
