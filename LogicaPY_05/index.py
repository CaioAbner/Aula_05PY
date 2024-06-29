# Avaliação de Shield e Vida - atv01 (chatGPT)

# player_life = int(input('Digite a quantidade de vida que você possui: '))
# player_shield = int(input('Digite a quantidade de shield que você possui: '))

# if (player_life < 50):
#     print(f'Cuidado, vida baixa')
# elif (player_shield < 50):
#     print(f'Shield baixo')
# elif (player_life > 50 and player_shield > 50):
#     print(f'Você está em boas condições')
# else:
#     print(f'Você morreu!')

# Escolha de Armas - atv02 (chatGPT)

# numero_de_inimigos = int(input('Digite a quantidade de inimigos próximos a você: '))

# if (numero_de_inimigos == 1 or numero_de_inimigos == 2):
#     print(f'Leve uma shotgun!')
# elif (numero_de_inimigos >= 3 and numero_de_inimigos <= 5):
#     print(f'Leve uma Assault Rifle!')
# elif (numero_de_inimigos > 5):
#     print(f'Leve uma bazuza!')

# Decisão de Cura - atv03 (chatGPT)

# vida_do_jogador = int(input('Digite a sua quantidade de vida: '))

# if (vida_do_jogador < 30):
#     print(f'Use um Medkit')
# elif (vida_do_jogador >= 3 and vida_do_jogador <= 75):
#     print(f'Use Bandagens')
# elif (vida_do_jogador > 75):
#     print(f'Não é necessário usar itens de cura')

# Gestão de Recursos - atv04 (chatGPT)

# qtd_madeira = int(input('Digite a quantidade de madeira que você possui: '))
# qtd_pedra = int(input('Digite a quantidade de pedra que você possui: '))
# qtd_metal = int(input('Digite a quantidade de metal que você possui: '))

# if (qtd_madeira < 100):
#     print(f'Recolha mais madeira, você possui somente {qtd_madeira}')
# elif (qtd_pedra < 100):
#     print(f'Recolha mais pedra, você tem somente {qtd_pedra}')
# elif (qtd_metal < 100):
#     print(f'Recolha mais metal, você possui somente {qtd_metal}')
# elif (qtd_madeira > 100 or qtd_pedra > 100 or qtd_metal > 100):
#     print(f'A quantidade de seus materiais estão boas')

# DESAFIO (SENHA FORTE)

qtd_req = 0

while True:
    menu = int(input('Digite a ação que deseja realizar \n 1 - Digitar senha \n 2 - Fechar programa \n'))

    senha_usuario = str(input('Digite sua senha: '))

    req_1 = len(senha_usuario) >= 8
    req_2 = '1234567890'
    req_3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    req_4 = 'abcdefghijklmnopqrstuvwxyz'
    req_5 = '%$¨&*()[]}{^~:;/?°|!#@'

    if (senha_usuario in req_1):

        print(qtd_req)
    if (qtd_req == 1 or qtd_req == 2):
        print(f'Senha fraca 😢')
    elif (qtd_req == 3 or qtd_req == 4):
        print(f'Senha média 🤔')
    elif (qtd_req == 5):
        print(f'Senha forte engual eu 😎🙌')

# DESAFIO NÚMERO ALEATÓRIO

# import random

# numero_aleatorio = random.randint(1, 100)

# while True:

#     numero_do_usuario = int(input('Digite um número: '))

#     if (numero_do_usuario < numero_aleatorio):
#         print(f'O número que você digitou é MENOR que o número aleatório!')
#     elif (numero_do_usuario > numero_aleatorio):
#         print(f'O número que você digitou é MAIOR que o número aleatório!')
#     elif (numero_do_usuario == numero_aleatorio):
#         print(f'O número que você digitou é IGUAL que o número aleatório!')
#         break