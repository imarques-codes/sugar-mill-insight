import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def treinar():
    # 1. Carregar os dados que geramos no passo anterior
    df = pd.read_csv('data/dados_brutos_usina.csv')
    
    # 2. Limpeza de Negócio: Só treinamos com a usina rodando (Safra)
    df_safra = df[df['moagem_t'] > 0].copy()
    
    # 3. Engenharia de Atributos: Criando a variável de impureza total
    df_safra['impureza_total'] = df_safra['impureza_mineral'] + df_safra['impureza_vegetal']
    
    # 4. Definir o que queremos prever (Target) e o que usaremos para prever (Features)
    features = ['moagem_t', 'atr_kg_t', 'impureza_mineral', 'impureza_vegetal', 'ph_caldo', 'impureza_total']
    target = 'rtc_eficiencia'
    
    X = df_safra[features]
    y = df_safra[target]
    
    # 5. Dividir dados em Treino (80%) e Teste (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 6. Criar e treinar o modelo
    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    print("⏳ Treinando o modelo de RTC... Por favor, aguarde.")
    modelo.fit(X_train, y_train)
    
    # 7. Avaliar a precisão
    previsoes = modelo.predict(X_test)
    erro = mean_absolute_error(y_test, previsoes)
    score = r2_score(y_test, previsoes)
    
    print(f"✅ Modelo Treinado!")
    print(f"📊 Erro Médio: {erro:.2f}% de RTC")
    print(f"📈 Precisão (R²): {score:.2f}")
    
    # 8. Salvar o "Cérebro" para usar no Dashboard depois
    joblib.dump(modelo, 'data/modelo_final.pkl')
    joblib.dump(features, 'data/lista_features.pkl')
    print("💾 Arquivos salvos na pasta 'data'!")

if __name__ == "__main__":
    treinar()