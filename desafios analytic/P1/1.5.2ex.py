def numeros_vezes(n):
    for i in range(1, n + 1):
        for num in range(i):
            print(f"{i} ", end=' ')
        print("")

numeros_vezes(5)