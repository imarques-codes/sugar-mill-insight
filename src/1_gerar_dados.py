import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def gerar_dados_usina(n_dias=730):
    """Gera dados sintéticos baseados na realidade de uma usina sucroalcooleira."""
    np.random.seed(42)
    inicio = datetime(2024, 1, 1)
    datas = [inicio + timedelta(days=i) for i in range(n_dias)]
    
    # Criando as colunas
    data = {
        'data': datas,
        'moagem_t': np.random.normal(12000, 2000, n_dias),  # Toneladas moídas
        'atr_kg_t': np.random.uniform(120, 150, n_dias),   # Açúcar Total Recuperável
        'impureza_mineral': np.random.uniform(0.5, 6.0, n_dias), 
        'impureza_vegetal': np.random.uniform(2.0, 10.0, n_dias),
        'ph_caldo': np.random.uniform(5.5, 7.5, n_dias)
    }
    
    df = pd.DataFrame(data)
    
    # Lógica de Negócio: O RTC é afetado negativamente pelas impurezas
    # e positivamente pelo ATR.
    df['rtc_eficiencia'] = (
        85 + (df['atr_kg_t'] * 0.05) 
        - (df['impureza_mineral'] * 0.7) 
        - (df['impureza_vegetal'] * 0.3) 
        + np.random.normal(0, 0.4, n_dias)
    )
    
    # Simular Entressafra (Janeiro e Fevereiro a usina para)
    df.loc[df['data'].dt.month.isin([1, 2]), ['moagem_t', 'rtc_eficiencia']] = 0
    
    return df

if __name__ == "__main__":
    # Garante que a pasta data existe
    if not os.path.exists('data'):
        os.makedirs('data')
        
    df_usina = gerar_dados_usina()
    df_usina.to_csv('data/dados_brutos_usina.csv', index=False)
    print("✅ Sucesso: Arquivo 'data/dados_brutos_usina.csv' gerado!")