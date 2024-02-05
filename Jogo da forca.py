palavra = 'PIPOCA' # Você pode escolher qualquer palavra
letra_usuario = []
chance = 3
ganhar = False

print('-='*12)
print('     JOGO DA FORCA')
print('-='*12)
print(' ')

while True:
    for letra in palavra:
        if letra.upper() in letra_usuario:
            print(letra, end= " ")
        else:
            print('_' , end=" ")
    print(f'Você tem {chance} Chances')

    tentativa = input('Escolha uma Letra para Advinhar: ')
    letra_usuario.append(tentativa.upper())

    if tentativa.upper() not in palavra.upper():
        chance -= 1

    ganhar = True
    for letra in palavra:
        if letra.upper() not in letra_usuario:
            ganhar = False
    
    if chance == 0 or ganhar:
        break


if ganhar:
    print(f'Parabéns, Voçê Ganhou! A palavra era: {palavra}')
else:
    print(f'Voçê perdeu! A palavra era: {palavra}')
