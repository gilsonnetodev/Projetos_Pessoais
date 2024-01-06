def linh():
    print('-='*12)


itens = {'ALICATE': 'R$13,99', 'MARTELO': 'R$19,00', 'FURADEIRA': 'R$120,00', 'PÁ': 'R$31,70'}
lista = itens.copy()
linh()
print('   LOJA DE CONSTRUÇÃO   ')
linh()
while True:
    linh()
    print('''[1] Pesquisar valor dos produtos
[2] Retirar itens
[3] Sair''')
    linh()
    while True:
        try:
            resposta = int(input('Selecione uma opção: '))
        except:
            print('Erro inesperado!')
        else:
            break
    if resposta == 1:
        pesq = str(input('Digite o item para ver seu Preço: ')).upper()
        if pesq not in itens:
            print('Produto inválido')
        else:
            print(f'O item {pesq} custa {lista[pesq]}')
    if resposta == 2:
        tirar = str(input('Qual item deseja retirar do catálogo? ')).upper()
        if tirar not in itens:
            print('Produto inválido')
        else:
            del itens[tirar]
            print(f'Produto removido!')
    if resposta == 3:
        print('Programa Finalizado!')
        break