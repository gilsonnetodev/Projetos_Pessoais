from tkinter import *

def click_button(numero):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(END, str(atual) + str(numero))

def click_ponto():
    visor.insert(END, '.')

def deletar():
    visor.delete(0, END)

def click_soma():
    primeiro = visor.get()
    global p_numero
    global matematica
    matematica = "soma"
    p_numero = float(primeiro)
    visor.delete(0,END)

def click_sub():
    primeiro = visor.get()
    global p_numero
    global matematica
    matematica = "subtracao"
    p_numero = float(primeiro)
    visor.delete(0,END)

def click_div():
    primeiro = visor.get()
    global p_numero
    global matematica
    matematica = "dividir"
    p_numero = float(primeiro)
    visor.delete(0,END)

def click_mult():
    primeiro = visor.get()
    global p_numero
    global matematica
    matematica = "multiplicar"
    p_numero = float(primeiro)
    visor.delete(0,END)

def click_igual():
    segundo = visor.get()
    visor.delete(0, END)
    if matematica == "soma":
        visor.insert(0, p_numero + float(segundo))
    if matematica == "subtracao":
        visor.insert(0, p_numero - float(segundo))
    if matematica == "multiplicar":
        visor.insert(0, p_numero * float(segundo))
    try:
        if matematica == "dividir":
            visor.insert(0, p_numero / float(segundo))
    except:
        visor.delete(0, END)
        visor.insert(END, str('Error'))


janela = Tk()
janela.title('Calculadora')
janela.resizable(False,False)
janela.geometry('280x380')
janela.configure(background= '#404040')

nome = Label(janela, text='CALCULADORA' , font= ('verdana', 15, 'bold'), padx = 10, pady = 10,
bg = '#404040', foreground= 'white')
nome.pack()

visor = Entry(janela,font= 'arial 15', bg= '#003399', fg= '#ffffff')
visor.pack()

bnt1 = Button(janela, text='1', background='#003399', bd= 4, pady = 14, padx= 14 , 
command= lambda: click_button(1), fg= '#ffffff')
bnt1.place(x=10, y=100)

bnt2 = Button(janela, text='2', background='#003399', bd= 4, pady = 14, padx= 14, 
command= lambda: click_button(2), fg= '#ffffff')
bnt2.place(x=10, y=155)

bnt3 = Button(janela, text='3', background='#003399', bd= 4, pady = 14, padx= 14, 
command= lambda: click_button(3), fg= '#ffffff')
bnt3.place(x=10, y=210)

bnt0 = Button(janela, text='0', background='#003399', bd= 4, pady = 14, padx= 14, 
command= lambda: click_button(0), fg= '#ffffff')
bnt0.place(x=10, y=265)

bnt4 = Button(janela, text='4', background='#003399', bd= 4, pady = 14, padx= 14, 
command= lambda: click_button(4), fg= '#ffffff')
bnt4.place(x=60, y=100)

bnt5 = Button(janela, text='5', background='#003399', bd= 4, pady = 14, padx= 14, 
command= lambda: click_button(5), fg= '#ffffff')
bnt5.place(x=60, y=155)

bnt6 = Button(janela, text='6', background='#003399', bd= 4, pady = 14, padx= 14, 
command= lambda: click_button(6), fg= '#ffffff')
bnt6.place(x=60, y=210)

bntponto = Button(janela, text='.', background='#003399', bd= 4, pady = 14, padx= 44,
command= click_ponto, fg= '#ffffff')
bntponto.place(x=60, y=265)

bnt7 = Button(janela, text='7', background='#003399', bd= 4, pady = 14, padx= 14, 
command= lambda: click_button(7), fg= '#ffffff')
bnt7.place(x=110, y=100)

bnt8 = Button(janela, text='8', background='#003399', bd= 4, pady = 14, padx= 14, 
command= lambda: click_button(8), fg= '#ffffff')
bnt8.place(x=110, y=155)

bnt9 = Button(janela, text='9', background='#003399', bd= 4, pady = 14, padx= 14, 
command= lambda: click_button(9), fg= '#ffffff')
bnt9.place(x=110, y=210)

bntsoma = Button(janela, text='+', background='#003399', bd= 4, pady = 14, padx= 14,
command= click_soma, fg= '#ffffff')
bntsoma.place(x=160, y=100)

bntsubtracao = Button(janela, text='-', background='#003399', bd= 4, pady = 14, padx= 14,
command= click_sub, fg= '#ffffff')
bntsubtracao.place(x=160, y=155)

bntmultiplicar = Button(janela, text='x', background='#003399', bd= 4, pady = 14, padx= 14,
command= click_mult, fg= '#ffffff')
bntmultiplicar.place(x=160, y=210)

bntdividir = Button(janela, text='/', background='#003399', bd= 4, pady = 14, padx= 14,
command= click_div, fg= '#ffffff')
bntdividir.place(x=162, y=265)

bntce = Button(janela, text='CE', background='#b32d00', bd= 4, pady = 119, padx= 14,
command= deletar, fg= '#ffffff')
bntce.place(x=210, y=100)

bntigual = Button(janela, text='=', background='#006600', bd= 4, pady = 14, padx= 119,
command= click_igual, fg= '#ffffff')
bntigual.place(x=10, y=320)

janela.mainloop()