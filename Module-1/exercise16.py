import random

def gerar_numero_secreto():
    return random.randint(1, 10)

def processar_jogo():
    numero_secreto = gerar_numero_secreto()
    palpite = None

    tentativas_restantes = 5

    while tentativas_restantes > 0:
        palpite = int(input("Adivinhe o número entre 1 e 10: "))

        if palpite == numero_secreto:
            print("Voce acertou!")
            break
        elif palpite < numero_secreto:
            print(f"O número secreto é maior que {palpite}")
        else:
            print (f"O número secreto é menor que {palpite}")
        
        tentativas_restantes -= 1
        print(f"Voce errou. Tentativas restantes {tentativas_restantes}")

    if tentativas_restantes == 0:
        print(f"Voce perdeu. O número era: {numero_secreto}")

processar_jogo()

#15/10/2024 >< 
