senha_correta = "12345"
tentativa = ""

while tentativa != senha_correta:

    tentativa = input("Digite sua senha: ")

    if tentativa != senha_correta:
        print("Senha incorreta. Tente novamente.")

print("Acesso liberado")
