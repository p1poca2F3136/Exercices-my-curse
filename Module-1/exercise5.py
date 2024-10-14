#Contar as vogais e consoantes ><

#Solicita uma frase ao usuário
frase = input("Digite uma frase: ").lower() #A função lower() transforma a frase em letras minúsculas!

#Defina as vogais
vogais, contagem_de_vogais = "aeiou", 0

#Defina as consoantes
consoantes, contagem_de_consoantes = "qwrtypsdfghjklzxcvnm", 0

#Conta quantas vogais existem na frase
for letra in frase:
    if letra in vogais:
        contagem_de_vogais += 1
    #Conta quantas consoantes existem na frase
    if letra in consoantes:
        contagem_de_consoantes += 1


print(f"A frase contém {contagem_de_vogais} vogais e {contagem_de_consoantes} consoantes.")

