#Rodar um dado

import random

"""lista = [1, 2, 3, 4, 5, 6]

escolher_numero = random.choice(lista)

print(f'Rodou um dado de 6 lados, o resultado foi: {escolher_numero}')"""


def rolar_dado():
    return random.randint(1, 6)

resultado = rolar_dado()

print(f"O dado rolou, o resultado foi: {resultado}")
