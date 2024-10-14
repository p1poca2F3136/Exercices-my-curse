#Mensagem personalizada

def exibir_informações(nome, idade):

    print(f"Seu nome é {nome} e voce tem {idade} anos")


nome_do_usuário = input("Qual é seu nome: ")
idade_do_usuário = int(input("Digite sua idade: "))

exibir_informações(nome=nome_do_usuário, idade=idade_do_usuário)

