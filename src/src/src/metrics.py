import numpy as np
import pandas as pd

def calcular_iv(df, coluna_analisada, coluna_churn='cancelou'):
    """Calcula o Information Value (IV) de uma variável categórica."""
    tabela = pd.crosstab(df[coluna_analisada], df[coluna_churn]).reset_index()
    tabela.columns = [coluna_analisada, 'Não Cancelou', 'Cancelou']

    qtd_bons = tabela['Não Cancelou'].sum()
    qtd_maus = tabela['Cancelou'].sum()

    perc_bons = tabela['Não Cancelou'] / qtd_bons
    perc_maus = tabela['Cancelou'] / qtd_maus

    odds = perc_bons / perc_maus
    ln_odds = np.log(odds)
    iv = (perc_bons - perc_maus) * ln_odds

    return round(iv.sum(), 4)


def analisar_matriz_risco(df, coluna_servico):
    """Gera a matriz de risco financeiro (MRR Perdido) por faixa de ticket."""
    df_temp = df[['valor_mensal', 'cancelou', coluna_servico]].copy()
    df_temp['Ticket'] = pd.cut(df['valor_mensal'], bins=3, labels=['Baixo', 'Médio', 'Alto'], precision=0)
    df_temp['MRR Perdido'] = df_temp['valor_mensal'] * df_temp['cancelou']

    resumo = df_temp.groupby(['Ticket', coluna_servico], observed=False).agg(
        clientes=('cancelou', 'count'),
        cancelou=('cancelou', 'sum'),
        Taxa_Churn=('cancelou', 'mean'),
        MRR_perdido=('MRR Perdido', 'sum')
    )
    return resumo
