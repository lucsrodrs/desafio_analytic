import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_sem_selecao = pd.read_csv("idh_1991.csv")
df = pd.DataFrame(
    {"REGIOES" : df_sem_selecao.iloc[:, 0],
    "IDH" : df_sem_selecao.iloc[:, 1],
    }
)

def tarefa_1():
    x = df["REGIOES"].iloc
    y = df["IDH"]


    plt.barh(x, y, height = 0.85, color = "#000000")
    plt.show()
    return

def tarefa_2():
    # Como o proprio nome diz, hist, em outras palavras, quantas vezes se repete
    y = df["IDH"]
    plt.hist(y, color = "#000000")
    plt.show()

    return

def tarefa_3():
    df_sem_selecao = pd.read_csv("idh_1991.csv")
    df_com_tudo = pd.DataFrame(
        {"REGIOES" : df_sem_selecao.iloc[:, 0],
        "IDH1" : df_sem_selecao.iloc[:, 1],
        "IDH2" : df_sem_selecao.iloc[:, 3],
        "IDH3" : df_sem_selecao.iloc[:, 5],
        }
    )

    x = df_com_tudo["IDH1"]   #Transparencia
    plt.hist(x, color="#aafa23", alpha=0.5, label='IDH1') 
    x = df_com_tudo["IDH2"]
    plt.hist(x, color="#000000", alpha=0.5, label='IDH2') 
    x = df_com_tudo["IDH3"]
    plt.hist(x, color="#562efa", alpha=0.5, label='IDH3')
                                
    plt.legend()
    plt.xlabel("IDH")
    plt.ylabel("Frequencia")
    plt.title("Distribuicao do IDH")
    plt.show()
    
    return


tarefa_3()