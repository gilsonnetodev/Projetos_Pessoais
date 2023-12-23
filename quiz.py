from time import sleep
pontos = 0
def linha():
    print('-='*10)
def linha2():
    print('-='*30)


linha()
print('     QUIZ DO GN')
linha()
print('Olá! seja bem vindo ao Quiz do |GN|')
sleep(1)
print('Vamos testar seus conhecimentos sobre diversos assuntos!')
sleep(1)
print('Você está pronto?')
pronto = str(input('[S/N]: '))
sleep(0.5)
if pronto in 'Nn':
    print('Que pena... Até a próxima!')
else:
    print('Então vamos dar inicio ao QUIZ!!!')
    sleep(1)
    print('Serão 5 perguntas, cada uma valendo 10 pontos')
    sleep(1)
    print('Cada pergunta errada você perde 5 pontos')
    sleep(1)
    print('Vamos para a Primeira pergunta...')
    sleep(1.5)
    linha2()
    print('''1° DE QUEM É A FAMOSA FRASE "PENSO, LOGO EXISTO"?

a) Platão
b) Sócrates
c) Dom Pedro
d) Descartes''')
    sleep(0.5)
    resposta1 = str(input('Qual a alternativa correta? a/b/c/d: '))
    if resposta1 in 'Dd':
        print('Resposta...')
        sleep(1)
        print('CORRETA!!!')
        pontos += 10
        print('Você acaba de Ganhar 10 pontos! Parabêns!')
        print(f'Total de pontos = {pontos}')
    else:
        print('Resposta...')
        sleep(1)
        print('ERRADA!!!')
        pontos -= 5
        print('Você acaba de perder 5 pontos! Que pena...')
        print(f'Total de pontos = {pontos}')
    sleep(1)
    linha()
    print('''2° DE ONDE É A INVENÇÃO DO CHUVEIRO ELETRICO?

a) França
b) Brasil
c) Alemanha
d) India''')
    resposta2 = str(input('Qual a alternativa correta? a/b/c/d: '))
    if resposta2 in 'Bb':
        print('Resposta...')
        sleep(1)
        print('CORRETA!!!')
        pontos += 10
        print('Você acaba de Ganhar 10 pontos! Parabêns!')
        print(f'Total de pontos = {pontos}')
    else:
        print('Resposta...')
        sleep(1)
        print('ERRADA!!!')
        pontos -= 5
        print('Você acaba de perder 5 pontos! Que pena...')
        print(f'Total de pontos = {pontos}')
    sleep(1)
    linha()
    print('''3° EM QUE PERIODO DA HISTÓRIA O FOGO FOI DESCOBERTO?

a) Paleolítico
b) Neolítico
c) Idade Média
d) Periodo da pedra polida''')
    resposta3 = str(input('Qual a alternativa correta? a/b/c/d: '))
    if resposta3 in 'Aa':
        print('Resposta...')
        sleep(1)
        print('CORRETA!!!')
        pontos += 10
        print('Você acaba de Ganhar 10 pontos! Parabêns!')
        print(f'Total de pontos = {pontos}')
    else:
        print('Resposta...')
        sleep(1)
        print('ERRADA!!!')
        pontos -= 5
        print('Você acaba de perder 5 pontos! Que pena...')
        print(f'Total de pontos = {pontos}')
    sleep(1)
    linha()
    print('''4° QUEM É DE O AUTOR DE "O PRINCIPE"?

a) Leonardo Di Caprio
b) Arquemedes
c) Maquiavel
d) Machado de Assis''')
    resposta4 = str(input('Qual a alternativa correta? a/b/c/d: '))
    if resposta4 in 'Cc':
        print('Resposta...')
        sleep(1)
        print('CORRETA!!!')
        pontos += 10
        print('Você acaba de Ganhar 10 pontos! Parabêns!')
        print(f'Total de pontos = {pontos}')
    else:
        print('Resposta...')
        sleep(1)
        print('ERRADA!!!')
        pontos -= 5
        print('Você acaba de perder 5 pontos! Que pena...')
        print(f'Total de pontos = {pontos}')
    sleep(1)
    print('E agora, vamos para a última pergunta...')
    sleep(1)
    print('Preparado? Então aqui lá vai...')
    sleep(2)
    linha()
    print('''5° QUAIS AS MAIORES PANDEMIAS DA HISTÓRIA?

a) Peste Negra e Covid-19
b) Variola e Hipertenção
c) Gripe Espanhola e Câncer
d) Aedes Aegypti e Chikungunya''')
    resposta5 = str(input('Qual a alternativa correta? a/b/c/d: '))
    if resposta5 in 'Aa':
        print('Resposta...')
        sleep(1)
        print('CORRETA!!!')
        pontos += 10
        print('Você acaba de Ganhar 10 pontos! Parabêns!')
    else:
        print('Resposta...')
        sleep(1)
        print('ERRADA!!!')
        pontos -= 5
        print('Você acaba de perder 5 pontos! Que pena...')
    sleep(1)
print(f'Parabêns! Você concluiu o Quiz do |GN| com um total de {pontos} pontos!')
sleep(1.2)
print('Obrigado pela Participação!')