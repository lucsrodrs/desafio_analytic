competidores = ["Joao", "Carlos", "Patricia", "Caio", "Leticia"]

competidores_cargos = {
    "Joao" : "Competicao",
    "Carlos" : "Desenvolvimento",
    "Patricia" : "Competicao",
    "Caio" : "Competicao",
    "Leticia" : "Gestao"
}

nome = input("Digite um nome para procura: ")
achou = 0

for percorre in competidores:
    if(percorre == nome):
        achou = 1

if(achou == 1):
    print(f"{nome} - {competidores_cargos[nome]}")
else:
    print("Nao encontramos na nossa base de dados")