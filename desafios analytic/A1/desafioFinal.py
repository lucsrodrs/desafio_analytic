import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_sem_selecao = pd.read_csv("Dataset_Processo_Seletivo_UFRJ_Analytica_2024-2.csv")

df = pd.DataFrame( 
    {
    "REGIOES": df_sem_selecao['sigla_uf'].unique(),
    "IDH 1991": df_sem_selecao.loc[df_sem_selecao['ano'] == 1991, 'idhm'].values,
    "Expc. Vida 1991": df_sem_selecao.loc[df_sem_selecao['ano'] == 1991, 'expectativa_vida'].values,
    "IDH 2000": df_sem_selecao.loc[df_sem_selecao['ano'] == 2000, 'idhm'].values,
    "Expc. Vida 2000": df_sem_selecao.loc[df_sem_selecao['ano'] == 2000, 'expectativa_vida'].values,
    "IDH 2010": df_sem_selecao.loc[df_sem_selecao['ano'] == 2010, 'idhm'].values,
    "Expc. Vida 2010": df_sem_selecao.loc[df_sem_selecao['ano'] == 2010, 'expectativa_vida'].values,     
    }
)


def diferenca_expectativa_vida():
    # 1991
    x = df["REGIOES"]
    y = df["Expc. Vida 1991"]
    plt.scatter(x, y, color="#FF0000", alpha=0.7, label="IDH 1991")

    # 2010
    x = df["REGIOES"]
    y = df["Expc. Vida 2000"]
    plt.scatter(x, y, color="#00FF00", alpha=0.7, label="IDH 2010")

    plt.legend()
    plt.xlabel("Regioes")
    plt.ylabel("IDH")
    plt.title("Distribuicao do IDH por Regiao")
    plt.show() 
    return

def diferenca_10anos_1991_2010():
    diferenca = pd.DataFrame(
        {
            "REGIOES": df["REGIOES"],
            "Diferenca": df["Expc. Vida 2010"] - df["Expc. Vida 1991"],
        }
    )

    filtro = diferenca["Diferenca"] >= 10
    diferenca_filtrada = diferenca[filtro]

    plt.bar(diferenca_filtrada["REGIOES"], diferenca_filtrada["Diferenca"], color='green')
    plt.xlabel("Regioes")
    plt.ylabel("Diferenca de expectativa de vida (anos)")
    plt.title("Estados com aumento de pelo menos 10 anos na expectativa de vida (1991-2010)")
    plt.show()

#print(df)

diferenca_expectativa_vida()
diferenca_10anos_1991_2010()
