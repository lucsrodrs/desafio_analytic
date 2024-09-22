#   ANOTACOES:
# pd.DataFrame nos permite dar nomes nas colunas, e caso eu queria acessar uma e so falar
# iloc nos permite se igual ao Slicing normal, porem apropriado para o panda/dataframe
# myvar = pd.Series() consigo ter o mesmo resultado com o dataframe, porem com algumas complicacoes para mais personalizacao
# alem disso, o myvar da pra colocar o index = ["..", ".." ...] para personalizar as linhas
#   df[’col1’] # obtem a coluna ’col1’
#   df.loc[:, ’col1’] obtem todos os elementos da coluna ’col1’
#   df.loc[:,’col1’:’col3’] obtem as colunas de ’col1’ ate ’col3’
#   Obs: a selecao e feita pegando todas as colunas entre as duas passadas, desconsiderando os nomes das colunas em si.
#   Na pratica, o panda pega um arquivo e consegue extrair as informacoes necessarios que o usuario necessita
#   Normalmente sao arquivos csv, json, txt, etc.
#   Comando para ler o arquivo: df = pd.read_csv("arquivo.csv")


import pandas as pd

dias_numeros = [1,2,3,4,5,6,7]
dias_nomes = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]
idades = [12, 21, 11, 5, 18, 23, 12, 21]
nomes = ["A", "B", "C", "D", "E", "F", "G", "B"]

dfi = pd.DataFrame(
    {"Idade" : idades,
    "Nomes" : nomes,
    }
)

df = pd.DataFrame(
    {"Numeros": dias_numeros,
    "Nomes": dias_nomes,
    }
)

df_filtrado1 = dfi[dfi["Idade"] < 18]
filtro = dfi["Idade"] < 18
df_filtrado_inverso = dfi[filtro]

# Filtragem com 2 criterios

filtro1 = dfi["Idade"] == 12
filtro2 = dfi["Nomes"] == "A"
df_filtrado2 = dfi[ filtro1 & filtro2 ]

# Filtragem com 2 criterios [TIPO 2]

df_filtrado3 = dfi[ (dfi["Idade"] == 21) & (dfi["Nomes"] == "B") ]

def printar_test():
    #print('='*50)
    #print(df)
    #print('='*50)
    #print(df.head(5))
    #print('='*50)
    #print(df.tail(5))
    #print('='*50)
    #print(df.iloc[0:3])
    #print('='*50)
    #print(df.iloc[2:4])
    #print('='*50)
    #print(df.iloc[5:6])
    #print('='*50)
    # primeira coluna
    #print(df.iloc[:, 0])
    #print('='*50)
    #print(df.iloc[:, 1:2])
    #print('='*50)
    #print(df.iloc[1:3, 2:3]) 
    #print('='*50)
    #print(df.iloc[0,1])
    return 

print(f"Menores que 18 {df_filtrado1}")
print(f"Maiores que 18 {df_filtrado_inverso}")
print(f"MULTIPLOS {df_filtrado2}")
print(f"MULTIPLOS [TIPO 2] {df_filtrado3}")