num1 = int(input("Digite o primeiro numero: "))
while(num1 < 0 or num1 > 9):
    print("Numero fora do intervo!!")
    num1 = int(input("Digite novamente: "))

num2 = int(input("Digite o segundo numero: "))   
while(num2 < 0 or num2 > 9):
    print("Numero fora do intervo!!")
    num2 = int(input("Digite novamente: "))

print(f"A soma deu: {num1 + num2}")