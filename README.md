### SugarMill-Insights: Inteligência Artificial na Indústria Sucroalcooleira

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green)](#)

##  Visão Geral
O **SugarMill-Insights** é uma solução de *Analytics Engineering* aplicada à otimização da **Recuperação Total de Cristais (RTC)**. O projeto utiliza Machine Learning para prever a eficiência industrial com base na qualidade da cana-de-açúcar e em parâmetros operacionais críticos.

Este sistema resolve o desafio da variabilidade no rendimento industrial, permitindo que gestores antecipem perdas baseadas em indicadores como ATR e níveis de impurezas minerais e vegetais.

---

### Arquitetura e Fluxo de Trabalho

![Fluxo do Projeto](img/workflow_comentarios.png)

### Estrutura do Repositório
```text
projeto-usina-dados/
├── data/               # Dados brutos (.csv) e modelos treinados (.pkl)
├── img/                # Diagramas de arquitetura e prints do sistema
├── src/                # Scripts de inteligência do projeto
│   ├── 1_gerar_dados.py    # Simulador de safra e variáveis industriais
│   └── 2_treinar_modelo.py   # Pipeline de ML e treinamento
├── app.py              # Dashboard interativo (Streamlit)
├── requirements.txt    # Gerenciamento de dependências
└── README.md           # Documentação do projeto
```
Detalhamento das Fases
Fase 1: Ingestão e Simulação de Dados
Script: src/1_gerar_dados.py

Comentário de Negócio: O script simula a sazonalidade real da safra brasileira, incluindo a interrupção da moagem durante a entressafra e a correlação direta entre impurezas e a queda no RTC.

Destaque: Implementação de lógica estocástica para representar a variabilidade do campo.

Fase 2: Modelagem Preditiva
Script: src/2_treinar_modelo.py

Algoritmo: Random Forest Regressor.

Justificativa Técnica: Escolha baseada na robustez do modelo para processar relações não-lineares complexas, comum em processos químicos industriais.

Métricas: Validação via MAE (Erro Médio Absoluto) e R², fornecendo uma margem de confiança clara para a operação.

Fase 3: Deploy e Ferramenta de Decisão
Script: app.py

Interface: Dashboard interativo em Streamlit.

Impacto: Criação de um simulador de cenários "What-if", permitindo ajustes preventivos nos parâmetros do turno antes que as perdas ocorram.


