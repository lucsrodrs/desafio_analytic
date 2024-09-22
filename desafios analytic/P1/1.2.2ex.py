num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if(num1 > num2):
    print(f"O maior numero e {num1}")
elif(num1 < num2):
    print(f"O maior numero e {num2}")
else:
    print("Numeros iguais")