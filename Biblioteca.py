from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def adicionar():
    if id.get == "" or titulo.get() == "" or autor.get() == "" or ano.get() == "":
        messagebox.showerror(title= 'ERRO', message=' Digite todos os Dados')
        return
    tv.insert('', 'end', values= (id.get(),titulo.get(), autor.get(), ano.get()))
    messagebox.showinfo(title= '', message= 'Livro Adicionado com sucesso')
    autor.delete(0,END)
    titulo.delete(0,END)
    ano.delete(0,END)
    id.delete(0,END)

def remover():
    try:
        itemSelect = tv.selection()[0]
        valores = tv.item(itemSelect, 'values')
    except:
        messagebox.showerror(title= 'ERRO', message='Selecione um Item para Remover')
    tv.delete(itemSelect)


janela = Tk()
janela.title('')
janela.geometry('500x400')
janela.resizable(False,False)
janela.config(bg= '#003d99')

nome_projeto = Label(janela,text= 'Registro de Livros', bg='#003d99', fg='#ffffff',
font= 'play 20')
nome_projeto.place(x=130, y=5)

texto_titulo = Label(janela,text= 'Título:', bg='#003d99', fg='#ffffff',
font= 'play 14')
texto_titulo.place(x=35, y=45)

titulo = Entry(janela, font= 'play 14', width= 18, bg='#333333', fg= '#ffffff')
titulo.place(x=105, y=45, height=28)

texto_autor = Label(janela,text= 'Autor:', bg='#003d99', fg='#ffffff',
font= 'play 14')
texto_autor.place(x=35, y=90)

autor = Entry(janela, font= 'play 14', width= 18, bg='#333333', fg= '#ffffff')
autor.place(x=105, y=90, height=28)

texto_ano = Label(janela,text= 'Ano:', bg='#003d99', fg='#ffffff',
font= 'play 14')
texto_ano.place(x=350, y=45)

ano = Entry(janela, font= 'play 15', width= 6, bg='#333333', fg= '#ffffff')
ano.place(x=400, y=45, height=28)

texto_id = Label(janela,text= 'ID:', bg='#003d99', fg='#ffffff',
font= 'play 14')
texto_id.place(x=350, y=90)

id = Entry(janela, font= 'play 15', width= 6, bg='#333333', fg= '#ffffff')
id.place(x=400, y=90, height=28)

bnt_adicionar = Button(janela,text='Adicionar Livro', font='play 15', bg='#0a0a0a', fg='#ffffff',
bd = 4, overrelief='ridge', command= adicionar)
bnt_adicionar.place(x=60, y=130, width=150, height=35)

bnt_remover = Button(janela,text='Remover Livro', font='play 15', bg='#0a0a0a', fg='#ffffff',
bd = 4, overrelief='ridge', command= remover)
bnt_remover.place(x=300, y=130, width=150, height=35)


tv = ttk.Treeview(janela, columns=('id','Título', 'Autor', 'Ano',), show= 'headings')
tv.column('id', minwidth=0, width= 100)
tv.column('Título', minwidth=0, width= 120)
tv.column('Autor', minwidth=0, width= 120)
tv.column('Ano', minwidth=0, width= 100)

tv.heading('id', text= 'id')
tv.heading('Título', text= 'Título')
tv.heading('Autor', text= 'Autor')
tv.heading('Ano', text= 'Ano')
tv.place(x=15, y=170, height=220, width=470)

janela.mainloop()
