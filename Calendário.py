from tkinter import ttk
import ttkbootstrap

janela = ttkbootstrap.Window(themename='cyborg')
janela.title('Calendário')

def ver_data():
    data = cal.entry.get()
    data_label.config(text= data)

cal = ttkbootstrap.DateEntry(janela, dateformat='%d/%m/%Y', bootstyle= 'info')
cal.pack(padx=40, pady=40)

bnt = ttk.Button(janela, text= 'Mostrar Data', bootstyle='ligth-outline', command= ver_data)
bnt.pack(padx=40, pady=40)

data_label = ttk.Label(janela, text='Sem data selecionada')
data_label.pack(padx=40, pady=40)

janela.mainloop()
