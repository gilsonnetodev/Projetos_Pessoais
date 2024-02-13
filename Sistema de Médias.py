from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def adicionar():

    if txt_numero.get() == '' or txt_nome.get() == '' or txt_media.get() == '':
        messagebox.showerror(title= 'ERRO', message=' Digite todos os Dados')
        return
    situacao = ''
    if float(txt_media.get()) >= 6:
         situacao = 'Aprovado'
    if float(txt_media.get()) < 6:
         situacao = 'Reprovado'

    tv.insert("", 'end', values= (txt_numero.get(), txt_nome.get(), txt_media.get(), situacao))

    txt_numero.delete(0,END)
    txt_nome.delete(0,END)
    txt_media.delete(0,END)

def remover():

    try:
        itemSelect = tv.selection()[0]
        valores = tv.item(itemSelect, 'values')
    except:
        messagebox.showerror(title= 'ERRO', message='Selecione um Item para Remover')

    tv.delete(itemSelect)


janela = Tk()
janela.title('')
janela.geometry('800x300')
janela.resizable(False,False)
janela.config(bg = '#003cb3')

lbl_titulo = Label(text='SISTEMA DE MÉDIAS', font= 'arial 22', bg= '#003cb3', fg= '#ffffff')
lbl_titulo.place(x=270,y=1)

lbl_numero = Label(text= 'N° do Aluno: ', font= 'arial 15', bg= '#003cb3', fg= '#ffffff')
lbl_numero.place(x=10,y=50)

txt_numero = Entry(janela,font= 'arial 15', bd= 4, bg= '#666666', fg= '#ffffff')
txt_numero.place(x=160, y=50, width=60)

lbl_nome = Label(janela, text='Nome do Aluno: ' ,font= 'arial 15',bg= '#003cb3', fg= '#ffffff')
lbl_nome.place(x=10,y=90)

txt_nome = Entry(janela,font= 'arial 15', bd= 4, bg= '#666666', fg= '#ffffff')
txt_nome.place(x=160, y=90, width=180)

lbl_media = Label(janela, text='Média Final: ' ,font= 'arial 15',bg= '#003cb3', fg= '#ffffff')
lbl_media.place(x=10,y=130)

txt_media = Entry(janela,font= 'arial 15', bd= 4, bg= '#666666', fg= '#ffffff')
txt_media.place(x=160, y=130, width=60)

bnt_adicionar = Button(janela, text= 'Adicionar', font= 'play 15', bg='#00802b', fg= '#ffffff',
    bd=4, command= adicionar)
bnt_adicionar.place(x=40, y=210, height=38)

bnt_remover = Button(janela, text= 'Remover', font= 'play 15', bg='#00802b', fg= '#ffffff',
    bd=4, command= remover)
bnt_remover.place(x=200, y=210, height=38)

tv = ttk.Treeview(janela, columns=('N° do Aluno', 'Nome do Aluno', 'Média Final', 'Situação'), show= 'headings')
tv.column('N° do Aluno', minwidth=0, width= 80)
tv.column('Nome do Aluno', minwidth=0, width= 120)
tv.column('Média Final', minwidth=0, width= 120)
tv.column('Situação', minwidth=0, width= 90)

tv.heading('N° do Aluno', text= 'N° do Aluno')
tv.heading('Nome do Aluno', text= 'Nome do Aluno')
tv.heading('Média Final', text= 'Média Final')
tv.heading('Situação', text= 'Situação')
tv.place(x=370, y= 40, height= 250)

janela.mainloop()
