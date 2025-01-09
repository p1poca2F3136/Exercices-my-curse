import random

def The_big_bang_theory():
    vitorias_usuario = 0
    vitorias_computador = 0
    empates = 0

    # Dicionário com as regras do jogo
    regras = {
        "1": ["3", "4"],  # Pedra quebra Tesoura e esmaga Lagarto
        "2": ["1", "5"],  # Papel embrulha Pedra e desqualifica Spock
        "3": ["2", "4"],  # Tesoura corta Papel e decapita Lagarto
        "4": ["2", "5"],  # Lagarto come Papel e envenena Spock
        "5": ["1", "3"]   # Spock vaporiza Pedra e quebra Tesoura
    }

    opcoes = {
        "1": "Pedra",
        "2": "Papel",
        "3": "Tesoura",
        "4": "Lagarto",
        "5": "Spock"
    }

    while True:
        print("\nEscolha uma opção:")
        input_do_usuario = input("1. Pedra\n2. Papel\n3. Tesoura\n4. Lagarto\n5. Spock\nSua escolha: ")

        if input_do_usuario not in opcoes:
            print("Opção inválida! Tente novamente.")
            continue

        escolha_aleatoria_do_computador = random.choice(list(opcoes.keys()))

        print(f"O computador escolheu: {opcoes[escolha_aleatoria_do_computador]}")

        if input_do_usuario == escolha_aleatoria_do_computador:
            print(f"Empate! Ambos escolheram {opcoes[input_do_usuario]}")
            empates += 1
        elif escolha_aleatoria_do_computador in regras[input_do_usuario]:
            print(f"Você ganhou! {opcoes[input_do_usuario]} vence {opcoes[escolha_aleatoria_do_computador]}.")
            vitorias_usuario += 1
        else:
            print(f"Você perdeu! {opcoes[escolha_aleatoria_do_computador]} vence {opcoes[input_do_usuario]}.")
            vitorias_computador += 1

        # Exibindo o placar
        print(f"Placar - Você: {vitorias_usuario} | Computador: {vitorias_computador} | Empates: {empates}")

        # Pergunta se o usuário quer jogar novamente
        jogar_novamente = input("Quer jogar novamente? (s/n): ")
        if jogar_novamente.lower() != 's':
            print("Obrigado por jogar!")
            break



# Função para jogar multiplayer
def multiplayer():
    vitorias_do_usuario_1 = 0  # Inicializa as vitórias do usuário 1
    vitorias_do_usuario_2 = 0  # Inicializa as vitórias do usuário 2
    empates = 0  # Inicializa a contagem de empates

    nome_do_usuario_1 = input("Usuário 1, digite seu nome de jogo: ")
    nome_do_usuario_2 = input("Usuário 2, digite seu nome de jogo: ")

    # O jogo continua até que o usuário queira parar
    while True:

        print(f"\nUsuário {nome_do_usuario_1}, escolha uma opção:")
        input_do_usuario_1 = input("1. Pedra\n2. Papel\n3. Tesoura\nSua escolha: ")
        print()
        input_do_usuario_2 = input(f"Usuário {nome_do_usuario_2}, escolha uma opção:\n1. Pedra\n2. Papel\n3. Tesoura\nSua escolha: ")

        # Lógica para empate
        if input_do_usuario_1 == input_do_usuario_2:
            print(f"Empate! Ambos escolheram {opcao_para_nome(input_do_usuario_1)}")
            empates += 1  # Se houver empate, aumenta a contagem de empates

        # Lógica para as vitórias de cada jogador
        elif (input_do_usuario_1 == "1" and input_do_usuario_2 == "3") or \
             (input_do_usuario_1 == "2" and input_do_usuario_2 == "1") or \
             (input_do_usuario_1 == "3" and input_do_usuario_2 == "2"):
            print(f"Usuário {nome_do_usuario_1} venceu! {opcao_para_nome(input_do_usuario_1)} vence {opcao_para_nome(input_do_usuario_2)}")
            vitorias_do_usuario_1 += 1  # Usuário 1 vence e sua contagem de vitórias aumenta

        elif (input_do_usuario_2 == "1" and input_do_usuario_1 == "3") or \
             (input_do_usuario_2 == "2" and input_do_usuario_1 == "1") or \
             (input_do_usuario_2 == "3" and input_do_usuario_1 == "2"):
            print(f"Usuário {nome_do_usuario_2} venceu! {opcao_para_nome(input_do_usuario_2)} vence {opcao_para_nome(input_do_usuario_1)}")
            vitorias_do_usuario_2 += 1  # Usuário 2 vence e sua contagem de vitórias aumenta

        # Exibe o placar após cada rodada
        print(f"\nPlacar - Usuário {nome_do_usuario_1}: {vitorias_do_usuario_1} | Usuário {nome_do_usuario_2}: {vitorias_do_usuario_2} | Empates: {empates}")

        # Pergunta se os jogadores querem continuar
        jogar_novamente = input("Querem jogar outra rodada? (s/n): ")
        if jogar_novamente.lower() != 's':  # Se qualquer jogador não quiser continuar
            print("Obrigado por jogar!")
            break  # Sai do loop e encerra o jogo

# Função auxiliar para converter a entrada numérica em nome da opção
def opcao_para_nome(opcao):
    if opcao == "1":
        return "Pedra"
    elif opcao == "2":
        return "Papel"
    elif opcao == "3":
        return "Tesoura"
    else:
        return "Opção inválida"

# Função para jogar o modo "Melhor de 3"
def iniciar_melhor_de_3():
    vitorias_usuario = 0
    vitorias_computador = 0
    empates = 0

    while vitorias_usuario < 3 and vitorias_computador < 3:
        print("\nEscolha uma opção:")
        input_do_usuario = input("1. Pedra\n2. Papel\n3. Tesoura\nSua escolha: ")

        escolha_para_o_computador = {"1": "Pedra", "2": "Papel", "3": "Tesoura"}
        escolha_aleatoria_do_computador = random.choice(list(escolha_para_o_computador.keys()))

        print(f"O computador escolheu: {escolha_para_o_computador[escolha_aleatoria_do_computador]}")

        # Lógica do jogo
        if input_do_usuario == escolha_aleatoria_do_computador:
            print(f"Empate! Ambos escolheram {escolha_para_o_computador[input_do_usuario]}")
            empates += 1
        elif input_do_usuario == "1" and escolha_aleatoria_do_computador == "3":
            print("Você ganhou! Pedra quebra Tesoura.")
            vitorias_usuario += 1
        elif input_do_usuario == "2" and escolha_aleatoria_do_computador == "1":
            print("Você ganhou! Papel embrulha Pedra.")
            vitorias_usuario += 1
        elif input_do_usuario == "3" and escolha_aleatoria_do_computador == "2":
            print("Você ganhou! Tesoura corta Papel.")
            vitorias_usuario += 1
        else:
            print(f"Você perdeu! {escolha_para_o_computador[escolha_aleatoria_do_computador]} vence {escolha_para_o_computador[input_do_usuario]}.")
            vitorias_computador += 1

        # Exibindo o placar
        print(f"Placar - Você: {vitorias_usuario} | Computador: {vitorias_computador} | Empates {empates}")

    if vitorias_usuario == 3:
        print("Você venceu a melhor de 3!")
    elif vitorias_computador == 3:
        print("O computador venceu a melhor de 3!")

    # Pergunta se o usuário quer jogar novamente
    jogar_novamente = input("Quer jogar novamente? (s/n): ")
    return jogar_novamente.lower() == 's'  # Retorna True ou False para reiniciar o jogo

# Função para jogar o modo "normal"
def iniciar_jogo():
    vitorias_usuario = 0
    vitorias_computador = 0
    empates = 0

    # Dicionário com as regras do jogo
    regras = {
        "1": ["3"],  # Pedra quebra Tesoura
        "2": ["1"],  # Papel embrulha Pedra
        "3": ["2"]   # Tesoura corta Papel
    }

    opcoes = {
        "1": "Pedra",
        "2": "Papel",
        "3": "Tesoura"
    }


    while True:
        print("\nEscolha uma opção:")
        input_do_usuario = input("1. Pedra\n2. Papel\n3. Tesoura\nSua escolha: ")

        if input_do_usuario not in opcoes:
            print("Opção inválida! Tente novamente.")
            continue

        escolha_aleatoria_do_computador = random.choice(list(opcoes.keys()))

        print(f"O computador escolheu: {opcoes[escolha_aleatoria_do_computador]}")

        if input_do_usuario == escolha_aleatoria_do_computador:
            print(f"Empate! Ambos escolheram {opcoes[input_do_usuario]}")
            empates += 1
        elif escolha_aleatoria_do_computador in regras[input_do_usuario]:
            print(f"Você ganhou! {opcoes[input_do_usuario]} vence {opcoes[escolha_aleatoria_do_computador]}.")
            vitorias_usuario += 1
        else:
            print(f"Você perdeu! {opcoes[escolha_aleatoria_do_computador]} vence {opcoes[input_do_usuario]}.")
            vitorias_computador += 1

        # Exibindo o placar
        print(f"Placar - Você: {vitorias_usuario} | Computador: {vitorias_computador} | Empates: {empates}")

        # Pergunta se o usuário quer jogar novamente
        jogar_novamente = input("Quer jogar novamente? (s/n): ")
        if jogar_novamente.lower() != 's':
            print("Obrigado por jogar!")
            break


# Função para exibir o placar final
def exibir_placar(vitorias_usuario, vitorias_computador):
    print(f"\nPlacar Final - Você: {vitorias_usuario} | Computador: {vitorias_computador}")

# Função para sair do programa
def sair_do_programa():
    print("Saindo... Até mais!")
    exit()

# Menu inicial do jogo
def menu_inicial():
    vitorias_usuario = 0
    vitorias_computador = 0

    while True:
        print("\n---- Menu Inicial ----")
        print("1. Jogar Pedra, Papel, Tesoura")
        print("2. Melhor de 3")
        print("3. Jogo Multiplayer")
        print("4. Modo The Big Bang Theory")
        print("5. Exibir Placar")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            iniciar_jogo()
        elif escolha == "2":
            # Loop que continua até o usuário decidir não jogar mais
            while True:
                if not iniciar_melhor_de_3():
                    break  # Sai do loop e volta ao menu inicial
        elif escolha == "3":
            multiplayer()  # Chama o modo multiplayer
        elif escolha == "4": # Chama modo The Big Bang Theory
            The_big_bang_theory()
        elif escolha == "5":
            exibir_placar(vitorias_usuario, vitorias_computador)
        elif escolha == "6":
            sair_do_programa()
        else:
            print("Opção inválida! Tente novamente.")

# Chama o menu inicial
menu_inicial()
