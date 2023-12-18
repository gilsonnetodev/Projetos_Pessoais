lista = []
def adicionar(*n):
    lista.append(*n)
    print('\033[32mTarefa Adicionada com Sucesso!\033[m')
def mostrar(*n):
    if not lista:
        print('\033[32mNenhuma tarefa pendente!\033[m')
    else:
        enumerate(lista)
        for i, item in enumerate(lista):
            print(f'{i}. {item}')
def linha():
    print('-='*15)
def concluir():
        if not lista:
            print('\033[31mTarefa não Existente\033[m')
        else:
            try:
                indice = int(input('\033[33mSelecione a Tarefa concluida: \033[m'))
                if 0 <= indice < len(lista):
                    conclusao = lista.pop(indice)
                    print(f'\033[32mTarefa "{conclusao}" concluida com sucesso!\033[m')
                else:
                    print('\033[31mTarefa não Existente\033[m')
            except:
                print('\033[31mTarefa não Existente\033[m')

linha()
print('\033[36m       LISTA DE TAREFAS\033[m')
linha()
while True:
    linha()
    print('''[1] Adicionar Tarefas
[2] Mostrar tarefas
[3] Concluir tarefa
[4] Sair''')
    linha()
    while True:
        try:
            resposta = int(input('\033[33mSelecione uma Opção: \033[m'))
            if resposta > 4 or resposta < 0:
                print('\033[31mOpção invalida! Tente novamente\033[m')
            else:
                break
        except:
            print('\033[31mOpção invalida! Tente novamente\033[m')
    if resposta == 1:
        adicionar(str(input('\033[33mAdicione sua tarefa: \033[m')))
    if resposta == 2:
        mostrar()
    if resposta == 3:
        mostrar()
        concluir()
    if resposta == 4:
        print('\033[32mObrigado! Volte sempre!\033[m') 
        break