#Verifica se a palavra ou frase é um Palíndromo

#Solicita uma frase
frase = input("Digite uma palavra ou frase: ").lower()

#Remova os espaços se for uma frase
frase = frase.replace(" ", "") #replace remove os espaços da frase

#Verifica se é palindromo
if frase == frase[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
