class ContaEmBanco():
    def __init__(self):
        self.saldo = 0
    def deposito(self,valor):
        self.saldo += valor
        print('\033[32mDeposito realizado com sucesso!\033[m')
        return self.saldo
    def retirar(self,valor):
        if self.saldo < valor:
            print(f'\033[31mSaldo indisponivel para saque! Seu saldo R${self.saldo}\033[m')
        else:
            self.saldo = self.saldo - valor
            print('\033[32mSaque realizado com sucesso!\033[m')
    def mostraSaldo(self):
        return self.saldo
def linha():
    print('-='*20)    


linha()
print('          CAIXA ELETRONICO')
linha()
dinheiro = ContaEmBanco()
while True: 
    linha()
    print('''    [1] Ver saldo 
    [2] Fazer um deposito 
    [3] Realizar um saque 
    [4] Sair do Caixa''') 
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
        print(f'\033[32mSeu saldo é de R${dinheiro.mostraSaldo()}\033[m')
    try:
        if resposta == 2:
            dinheiro.deposito(valor = float(input('\033[33mvalor do Deposito R$\033[m')))
    except:
            print('\033[31mErro! valor inválido!\033[m')
    try:
        if resposta == 3:
            dinheiro.retirar(valor= float(input('\033[33mDigite o valor do Saque R$\033[m')))
    except:
            print('\033[31mErro! valor inválido!\033[m')
    if resposta == 4:
        print('\033[32mObrigado! Volte sempre!\033[m')
        break