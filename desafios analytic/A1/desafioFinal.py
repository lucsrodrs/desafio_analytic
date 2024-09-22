import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_sem_selecao = pd.read_csv("Dataset_Processo_Seletivo_UFRJ_Analytica_2024-2.csv")
idh_1991 = df_sem_selecao[df_sem_selecao['ano'] == 1991][['sigla_uf', 'idhm', 'expectativa_vida']]
idh_2000 = df_sem_selecao[df_sem_selecao['ano'] == 2000][['sigla_uf', 'idhm', 'expectativa_vida']]
idh_2010 = df_sem_selecao[df_sem_selecao['ano'] == 2010][['sigla_uf', 'idhm', 'expectativa_vida']]


def diferenca_expectativa_vida():
    # 1991
    x = idh_1991['sigla_uf']
    y = idh_1991['idhm']
    plt.scatter(x, y, color="#FF0000", alpha=0.7, label="IDH 1991")

    # 2010
    x = idh_2010['sigla_uf']
    y = idh_2010['idhm']
    plt.scatter(x, y, color="#00FF00", alpha=0.7, label="IDH 2010")

    plt.legend()
    plt.xlabel("Regioes")
    plt.ylabel("IDH")
    plt.title("Distribuicao do IDH por Regiao")
    plt.show() 
    return

def diferenca_10anos_1991_2010():
    # Merged mescla os 2 dataframe. on e o que tem em comum e o suffixes e para diferencia entre eles. Ou seja, idhm agora esta acrescentado por _Ano a fim de melhor manipulacao
    merged = pd.merge(idh_1991, idh_2010, on='sigla_uf', suffixes=('_1991', '_2010'))
    
    # pd.to_numeric e para converter para numero, para poder fazer a operacao
    merged['Diferenca'] = pd.to_numeric(merged['expectativa_vida_2010'], errors='coerce') - pd.to_numeric(merged['expectativa_vida_1991'], errors='coerce')
    
    estados_aumentado = merged[merged['Diferenca'] >= 10]
    
    plt.bar(estados_aumentado['sigla_uf'], estados_aumentado['Diferenca'], color='green')


    plt.bar(estados_aumentado["sigla_uf"], estados_aumentado["Diferenca"], color='green')
    plt.xlabel("Regioes")
    plt.ylabel("Diferenca de expectativa de vida (anos)")
    plt.title("Estados com aumento de pelo menos 10 anos na expectativa de vida (1991-2010)")
    plt.show()

diferenca_expectativa_vida()
diferenca_10anos_1991_2010()