from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def cadastrar():
    if texto_nome.get() == "" or texto_cidade.get() == "" or texto_telefone.get() == "" or texto_codigo.get() == "":
        messagebox.showerror(title= 'ERRO', message=' Digite todos os Dados')
        return
    tv.insert("", 'end', values= (texto_codigo.get(), texto_nome.get(), texto_cidade.get(), texto_telefone.get()))
    texto_codigo.delete(0,END)
    texto_nome.delete(0,END)
    texto_cidade.delete(0,END)
    texto_telefone.delete(0,END)

def remover():
    itemSelect = tv.selection()[0]
    tv.delete(itemSelect)

    


janela = Tk()
janela.title('Cadastro de Clientes')
janela.geometry('720x600')
janela.config(bg= '#862d86')

titulo = Label(janela, text= 'Cadastro de clientes', font= 'play 20', bg='#862d86', fg= '#ffffff')
titulo.place(x=220, y= 10)

nome = Label(janela, text= 'Nome:', font= 'play 16', bg='#862d86', fg= '#ffffff')
nome.place(x=10, y=60)

texto_nome = Entry(janela, font= 'play 16', bg='#666666', fg= '#ffffff', bd= 4)
texto_nome.place(x=90, y= 60)

cidade = Label(janela, text= 'Cidade:', font= 'play 16', bg='#862d86', fg= '#ffffff')
cidade.place(x=8, y=110)

texto_cidade = Entry(janela, font= 'play 16', bg='#666666', fg= '#ffffff', bd= 4)
texto_cidade.place(x=90, y= 110)

telefone = Label(janela, text= 'Telefone:', font= 'play 16', bg='#862d86', fg= '#ffffff')
telefone.place(x=350, y= 60)

texto_telefone = Entry(janela, font= 'play 16', bg='#666666', fg= '#ffffff', bd= 4)
texto_telefone.place(x=450, y= 60)

codigo = Label(janela, text= 'Codigo:', font= 'play 16', bg='#862d86', fg= '#ffffff')
codigo.place(x=364, y= 110)

texto_codigo = Entry(janela, font= 'play 16', bg='#666666', fg= '#ffffff', bd= 4,)
texto_codigo.place(x=450, y= 110, width=50)

bnt_cadastrar = Button(text= 'Cadastrar', font= 'play 16', bg='#003cb3', fg= '#ffffff', bd= 4,
                        command= cadastrar)
bnt_cadastrar.place(x=160, y= 155, height= 38)

bnt_remover= Button(text= 'Remover', font= 'play 16', bg='#003cb3', fg= '#ffffff', bd= 4,
                    command= remover)
bnt_remover.place(x=430, y= 155, height= 38)

tv = ttk.Treeview(janela, columns=('Código', 'Nome', 'Cidade', 'Telefone',), show= 'headings')
tv.column('Código', minwidth=0, width= 60)
tv.column('Nome', minwidth=0, width= 200)
tv.column('Cidade', minwidth=0, width= 200)
tv.column('Telefone', minwidth=0, width= 200)

tv.heading('Código', text= 'Código')
tv.heading('Nome', text= 'Nome')
tv.heading('Cidade', text= 'Cidade')
tv.heading('Telefone', text= 'Telefone')
tv.place(x=28, y= 210, height=370)

janela.mainloop()
