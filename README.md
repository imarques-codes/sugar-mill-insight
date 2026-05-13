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

Para garantir o máximo de transparência e profissionalismo, o projeto foi estruturado seguindo um pipeline de dados claro, focado na escalabilidade e na facilidade de implantação industriais. O diagrama abaixo detalha o fluxo completo, desde a ingestão de dados brutos até a entrega de valor através de dashboards interativos.

<!-- INÍCIO DO BLOCO DA IMAGEM -->
<p align="center">
  <img src="img/arquitetura.png" alt="Diagrama de Arquitetura do Projeto SugarMill-Insights" width="100%">
  <br>
  <em>Figura 1: Diagrama detalhado do pipeline de dados, treinamento do modelo e aplicação final.</em>
</p>
<!-- FIM DO BLOCO DA IMAGEM -->

A arquitetura está dividida em três camadas principais:

1.  **Origem dos Dados e Cenário:** Camada de ingestão que gerencia dados históricos (CSV) e está preparada para integração com dados ao vivo (IoT/API), simulando o ambiente de uma usina real.
2.  **Processamento e Modelagem (ML Engine):** Onde os dados são tratados e o algoritmo **Random Forest Regressor** é treinado, validado (métricas MAE e R²) e serializado (.pkl).
3.  **Deploy e Aplicação:** Camada final que utiliza **Streamlit** para criar uma interface interativa, permitindo previsões de RTC em tempo real e simulações de cenários ("What-If") para suporte à decisão operacional.

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

**Execução do Pipeline:**
   | Ordem | Comando | Descrição |
   | :--- | :--- | :--- |
   | 1º | `python src/1_gerar_dados.py` | Gera o histórico de safra simulado |
   | 2º | `python src/2_treinar_modelo.py` | Treina a IA e exporta os arquivos `.pkl` |
   | 3º | `streamlit run app.py` | Inicializa a interface gráfica |

---

## Autor

**Igor Marques** - *Estudante de Engenharia de Software, especialização em DATA & AI.*

*igorhmsantos@gmail.com*.


---

### 📝 Licença
Este projeto é destinado a fins de portfólio. Desenvolvido para demonstrar a aplicação de inteligência artificial na melhoria de processos reais do agronegócio brasileiro.


