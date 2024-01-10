from tkinter import *

def somar():
    n1 = float(text_num1.get())
    n2 = float(text_num2.get())
    resultado = Label(fimframe, font= 'Arial 13',text= f'A Soma é {n1 + n2}')
    resultado.pack(padx= 10, pady= 10)

def subtrair():
    n1 = float(text_num1.get())
    n2 = float(text_num2.get())
    resultado = Label(fimframe, font= 'Arial 13',text= f'A Subtração é {n1 - n2}')
    resultado.pack(padx= 10, pady= 10)

def multiplicar():
    n1 = float(text_num1.get())
    n2 = float(text_num2.get())
    resultado = Label(fimframe, font= 'Arial 13',text= f'A Multiplicação é {n1 * n2}')
    resultado.pack(padx= 10, pady= 10)

def dividir():
    n1 = float(text_num1.get())
    n2 = float(text_num2.get())
    resultado = Label(fimframe,font= 'Arial 13',text= f'A Divisão é {n1 / n2}')
    resultado.pack(padx= 10, pady= 10)

janela = Tk()
janela.title('APP')
frame1 = Frame(janela)
frame2 = Frame(janela)
pc_frame = Frame(janela)
fimframe = Frame(janela)

num1 = Label(pc_frame, text= 'Primeiro Número', font= 'arial 13')
text_num1 = Entry(pc_frame, font= 'arial 13')
num2 = Label(pc_frame, text= 'Segundo Número', font= 'arial 13')
text_num2 = Entry(pc_frame, font= 'arial 13')

bnt_soma = Button(frame1, text='Somar', font='arial 13', command= somar)
bnt_subtrair = Button(frame1, text='Subtrair', font='arial 13', command= subtrair)
bnt_multi = Button(frame2, text='Multiplicar', font='arial 13', command= multiplicar)
bnt_dividir = Button(frame2, text='Dividir', font='arial 13', command= dividir)

num1.pack(padx= 10, pady= 10)
text_num1.pack(padx= 10, pady= 10)
num2.pack(padx= 10, pady= 10)
text_num2.pack(padx= 10, pady= 10)

bnt_soma.pack(padx= 10, pady= 10)
bnt_subtrair.pack(padx= 10, pady= 10)
bnt_multi.pack(padx= 10, pady= 10)
bnt_dividir.pack(padx= 10, pady= 10)
pc_frame.grid()
frame1.grid(row=1, sticky=W)
frame2.grid(row=1, sticky=E)
fimframe.grid()

janela.mainloop()