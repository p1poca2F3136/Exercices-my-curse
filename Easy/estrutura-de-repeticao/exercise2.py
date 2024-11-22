entrada = input("Digite 10 números separando-os com virgulas: ")

numeros = [int(numero) for numero in entrada.split(",")]

soma = sum(numeros)

print(f"A soma dos números é: {soma}")
