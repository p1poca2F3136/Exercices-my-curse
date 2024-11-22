import random 

tabuada = int(input("Digite o número da tabuada desejada: "))

while True:
    
    numero_aleatorio = random.randint(1, 10)

    formar_resposta = tabuada * numero_aleatorio

    resposta = int(input(f"Quanto é {tabuada} x {numero_aleatorio}: "))


    if resposta == formar_resposta:
        print("Você acertou!!")
    else:
        print(f"Você errou, a resposta era {formar_resposta}")

