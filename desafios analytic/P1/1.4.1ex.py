competidores = ["Joao", "Carlos", "Patricia", "Caio", "Leticia"]

nome = input("Digite um nome para procura: ")
achou = 0

for percorre in competidores:
    if(percorre == nome):
        achou = 1

if(achou == 1):
    print(f"Achamos o usuario {nome}")
else:
    print("Nao encontramos na nossa base de dados")