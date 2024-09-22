import pandas as pd

# Dados retirados do site https://www.fapespa.pa.gov.br/sistemas/pcn2015/tabelas/08_idhm/01_indice_de_desenvolvimento_humano_idh_segundo_unidades_da_federacao_1991_2000_2010.htm
# Solicitei para o chatgpt dar uma tratada no texto, para que coloque apenas virgulas entre os dados
df_sem_selecao = pd.read_csv("Dataset_Processo_Seletivo_UFRJ_Analytica_2024-2.csv")
# Desejo pegar apenas os valores do nome e o idh. Aproveitei e coloquei os nomes da coluna
df = pd.DataFrame( 
    {
    "REGIOES": df_sem_selecao['sigla_uf'].unique(),
    "IDH 1991": df_sem_selecao.loc[df_sem_selecao['ano'] == 1991, 'idhm'].values,
    "IDH 2000": df_sem_selecao.loc[df_sem_selecao['ano'] == 2000, 'idhm'].values,
    "IDH 2010": df_sem_selecao.loc[df_sem_selecao['ano'] == 2010, 'idhm'].values,
    }
)

def exercicio_1_2():
    # Primeiro iremos colocar os dados de um arquivo em um variavel que ira armazena-la
    # Vale ressaltar que essas dados foram tirados de um exemplo da w3schools.com
    # Caso eu queria visualizar a tabela toda devo descomentar essa linha:
    #pd.options.display.max_rows = 9999
    # 1 - Lendo um arquivo para dataframe
    minha_df = pd.read_csv("data.csv")
    # 2 - Visualizando os dados em tabela
    print(minha_df)
    return

def exercicio_3():
    #print(df)
    media = df["IDH 1991"].mean()
    print(f"MEDIA DE 1991: {media}")

def exercicio_4():
    media = df["IDH 1991"].mean()

    # A) B) Consegui filtar e imprimir junto com a regiao
    filtro_maior_media = df[df["IDH 1991"] > media]
    print(f"{filtro_maior_media}")


def exercicio_5():
    # Ordena apenas o de 1991
    df_ordenado = df.sort_values("IDH 1991")

    print(df_ordenado.head(5))

def exercicio_6():
    print(df["IDH 1991"])
    print(df["IDH 1991"].min())
    print(df["IDH 1991"].max())
    print(df["IDH 1991"].idxmin()) 
    print(df["IDH 1991"].idxmax())

exercicio_1_2()
exercicio_3()
exercicio_4()
exercicio_5()
exercicio_6()
