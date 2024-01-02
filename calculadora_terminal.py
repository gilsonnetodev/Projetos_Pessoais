def linha():
    print('-='*11)


linha()
print('     CALCULADORA')
linha()
while True:
    linha()
    print('''[1] SOMAR
[2] SUBTRAIR
[3] MULTIPLICAR
[4] DIVIDIR
[5] SAIR''')
    linha()
    try:
        resposta = int(input('Selecione a Operação: '))
        if resposta > 5 or resposta <= 0:
            print('\033[31mOpção invalida! Tente novamente\033[m')
    except:
        print('\033[31mOpção invalida! Tente novamente\033[m')
    if resposta == 1:
        a = float(input('Primeiro valor: '))
        b = float(input('Sugundo valor: '))
        print(f'\033[33m{a} + {b} = {a + b}\033[m')
    if resposta == 2:
        a = float(input('Primeiro valor: '))
        b = float(input('Sugundo valor: '))
        print(f'\033[33m{a} - {b} = {a - b}\033[m')
    if resposta == 3:
        a = float(input('Primeiro valor: '))
        b = float(input('Sugundo valor: '))
        print(f'\033[33m{a} * {b} = {a * b}\033[m')
    if resposta == 4:
        a = float(input('Primeiro valor: '))
        b = float(input('Sugundo valor: '))
        print(f'\033[33m{a} / {b} = {a / b}\033[m')
    if resposta == 5:
        print('Programa encerrado, Volte sempre!')
        break
