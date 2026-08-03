# 📉 Telco Customer Churn & Financial Risk Analysis

Projeto de análise exploratória e estratégica de cancelamento de clientes (Churn) utilizando técnicas estatísticas de crédito (**Information Value - IV**), análise financeira de receita recorrente (**MRR**) e identificação de alavancas de retenção.

---

## 🎯 Problema de Negócio

Em empresas do setor de telecomunicações, a retenção de clientes é crítica para manter a previsibilidade de receita. A aquisição de novos clientes pode custar até 5x mais do que a retenção da base atual. 

O objetivo deste projeto é diagnosticar os principais **fatores geradores de churn**, ranquear o **poder preditivo das variáveis** e identificar onde está a maior **perda financeira de receita recorrente (MRR)**.

---

## 💡 Principais Insights Encontrados

1. **Impacto da Fibra Óptica (Top Churn x MRR):**
   - Clientes com serviço de **Fibra Óptica** possuem uma taxa desproporcional de cancelamento quando comparados a conexões DSL, concentrando o maior volume de **MRR perdido** nos tickets médio e alto.
2. **Anomalia do Cross-Selling (Fricção no 1º Serviço):**
   - A contratação de apenas **1 serviço adicional** gera o maior pico de churn da base (**45,76%**). No entanto, a partir do 2º serviço adicional contratado, a taxa cai continuamente, demonstrando o **efeito de proteção e engajamento** do cross-selling maduro.
3. **Mês a Mês vs. Fidelidade:**
   - O tipo de contrato é a variável de maior poder de separação (**IV > 0.30**). Clientes sem contrato de longo prazo (*month-to-month*) representam o maior ponto de fragilidade da operação.
4. **Curva de Sobrevivência Inicial:**
   - O primeiro ano de contrato concentra a grande maioria das evasões, exigindo ações de *onboarding* focadas principalmente nos primeiros **3 a 6 meses**.

---

## 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python 3.12+
- **Manipulação e Análise:** Pandas, NumPy
- **Visualização de Dados:** Seaborn, Matplotlib
- **Métricas de Negócio:** Information Value (IV), MRR (Monthly Recurring Revenue), Taxa de Churn

---

## 📂 Estrutura do Repositório

```text
telco-analise-churn/
│
├── data/                       # Arquivos de dados do projeto
├── notebooks/
│   ├── exploratory/            # Rascunhos e análises iniciais do Kaggle
│   └── analise_churn.ipynb     # Notebook principal estruturado e formatado
├── src/                        # Módulos Python reutilizáveis
│   ├── __init__.py
│   ├── data_prep.py            # Tratamento, limpeza e engenharia de dados
│   └── metrics.py              # Cálculo de IV e Matriz de Risco Financeiro
├── .gitignore
└── README.md

```
## 👤 Autor

Desenvolvido por **Douglas Carmo dos Santos**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/carmo-douglas/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/carmo-douglas)
