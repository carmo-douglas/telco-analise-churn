import pandas as pd

def carregar_e_tratar_dados(caminho_csv):
    """
    Carrega o dataset da Telco, renomeia as colunas para PT-BR, 
    trata tipos de dados incorretos e padroniza as variáveis dummy.
    """
    df = pd.read_csv(caminho_csv)

    dicionario_colunas = {
        'customerID': 'id_cliente', 'gender': 'genero', 'SeniorCitizen': 'idoso',
        'Partner': 'tem_parceiro', 'Dependents': 'dependentes', 'tenure': 'meses_contrato',
        'PhoneService': 'servico_telefone', 'MultipleLines': 'multiplas_linhas',
        'InternetService': 'provedor_internet', 'OnlineSecurity': 'seguranca_online',
        'OnlineBackup': 'backup_online', 'DeviceProtection': 'protecao_dispositivo',
        'TechSupport': 'suporte_tecnico', 'StreamingTV': 'tv_streaming',
        'StreamingMovies': 'filmes_streaming', 'Contract': 'tipo_contrato',
        'PaperlessBilling': 'fatura_digital', 'PaymentMethod': 'forma_pagamento',
        'MonthlyCharges': 'valor_mensal', 'TotalCharges': 'valor_total', 'Churn': 'cancelou'
    }

    df = df.rename(columns=dicionario_colunas)

    # Tratamento de valores totais e nulos
    df['valor_total'] = pd.to_numeric(df['valor_total'], errors='coerce').fillna(0)

    # Mapeamento da variável alvo e tratamento do status de idoso
    df['cancelou'] = df['cancelou'].map({'Yes': 1, 'No': 0})
    df['idoso'] = df['idoso'].map({1: 'Yes', 0: 'No'})

    return df
