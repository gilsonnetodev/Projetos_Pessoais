from tkinter import *
from tkinter import messagebox

def adicionar():
    valor = tarefa.get()
    caixa.insert(END, valor)
    tarefa.delete(0,END)
    messagebox.showinfo(title= 'Checklist', message= 'Tarefa Adicionada com sucesso!' )

def remover():
    caixa.delete(ACTIVE)
    messagebox.showinfo(title= 'Checklist', message= 'Tarefa Removida com sucesso!' )

janela = Tk()
janela.title('Checklist')
janela.configure(background= '#404040')
janela.geometry('300x510')
janela.resizable(False,False)

txt = Label(janela, text= 'Checklist',font= 'verdana 25', fg= '#ffffff', bg= '#404040' )
txt.pack()

bnt1 = Button(text= 'Adicionar', font= 'arial 10', bg= 'green', bd=4, padx=5, command= adicionar)
bnt1.place(x= 45, y=50)

bnt2 = Button(text= 'Remover', font= 'arial 10', bg= 'red', bd=4, padx=5, command= remover)
bnt2.place(x=185, y=50)

tarefa = Entry(janela, font= 'arial 15', bg= 'light blue', bd=2)
tarefa.place( x=35, y=90)

caixa = Listbox(janela, width=28, height= 18, bg= 'light blue', font= 'arial 13')
caixa.place(x=20, y= 130)

janela.mainloop()
