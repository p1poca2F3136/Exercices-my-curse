#Calculadora de média com Resultado ><

def calcular_media( nota_1, nota_2, nota_3):
    return (nota_1 + nota_2 + nota_3) / 3

def avaliar_media(media):
    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    elif media <= 4:
        print("Reprovado")
    else:
        print("Parametros invalidos!")

nota_1 = int(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
nota_3 = int(input("Digite a tercira nota: "))

media = calcular_media(nota_1, nota_2, nota_3)

print(f"Média do aluno: {media:.2f}")
avaliar_media(media)

#02/11/2024
