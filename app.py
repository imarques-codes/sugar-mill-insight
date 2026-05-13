import streamlit as st
import pandas as pd
import joblib
import os

# 1. Configuração da Página
st.set_page_config(page_title="Usina BioEnergia - Predição RTC", layout="wide")

# Título e Descrição
st.title("Monitoramento Preditivo: Eficiência Industrial (RTC) " \
"Elaborado por Igor Marques")
st.markdown("""
Esta aplicação utiliza um modelo para prever a Recuperação Total de Cristais (RTC) 
com base nos parâmetros de entrada da moagem e laboratório.
""")

# 2. Carregar o Modelo e a Lista de Variáveis
@st.cache_resource
def carregar_recursos():
    if os.path.exists('data/modelo_final.pkl'):
        modelo = joblib.load('data/modelo_final.pkl')
        features = joblib.load('data/lista_features.pkl')
        return modelo, features
    return None, None

modelo, features_list = carregar_recursos()

if modelo is None:
    st.error("❌ Modelo não encontrado! Por favor, execute primeiro o script 'src/2_treinar_modelo.py'.")
else:
    # 3. Painel de Controle Lateral (Inputs)
    st.sidebar.header("Painel de Controle do Turno")
    
    moagem = st.sidebar.number_input("Moagem Atual (t/dia)", 5000, 20000, 12000)
    atr = st.sidebar.slider("Qualidade da Cana (ATR)", 110.0, 160.0, 135.0)
    imp_min = st.sidebar.slider("Impureza Mineral (%)", 0.0, 10.0, 2.5)
    imp_veg = st.sidebar.slider("Impureza Vegetal (%)", 0.0, 15.0, 5.0)
    ph = st.sidebar.slider("pH do Caldo", 4.0, 9.0, 6.8)
    
    # 4. Processamento da Predição
    dados_usuario = pd.DataFrame({
        'moagem_t': [moagem],
        'atr_kg_t': [atr],
        'impureza_mineral': [imp_min],
        'impureza_vegetal': [imp_veg],
        'ph_caldo': [ph],
        'impureza_total': [imp_min + imp_veg]
    })

    predicao = modelo.predict(dados_usuario)[0]

    # 5. Exibição dos Resultados
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="RTC Estimado para o Turno", value=f"{predicao:.2f} %")
        
        if predicao < 88.5:
            st.warning("⚠️ Alerta: Rendimento abaixo da meta histórica!")
        else:
            st.success("✅ Rendimento dentro dos padrões de eficiência.")

    with col2:
        st.subheader("Análise de Impacto")
        st.write("O modelo identificou que a combinação atual de impurezas e ATR resultará na eficiência acima.")

    