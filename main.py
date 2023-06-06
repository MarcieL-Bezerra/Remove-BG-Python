import sys
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fdlg
import tkinter.messagebox as tkMessageBox
from tkinter import *
from script import removeBG

def RemoveBG():
	
    try:
        #aqui seleciona os arquivos
        #nomedoarquivo = TxtOrigem.get()
        #path = fdlg.askopenfilenames()
        #df = pd.DataFrame()
        #aqui seleciona a pasta a ser colocada o novo arquivo
        TxtDestino.config(state='normal')
        TxtOrigem.config(state='normal')
        # comboFormato.config(state='normal')
        TxtOrigem.delete(0,"end")
        TxtDestino.delete(0,"end")

        LblStatus.grid(row=11,column=1)
        LblStatus.configure(text = "Aguarde ... ...")
        
        tkMessageBox.showinfo("Selecionar Pasta", message= "Selecione Pasta de Origem!")
        opcoes = {}                # as opções são definidas em um dicionário
        opcoes['initialdir'] = ''    # será o diretório atual
        opcoes['parent'] = tinicial
        opcoes['title'] = 'Selecione Pasta para salvar!'
        caminhoOrigem = fdlg.askdirectory(**opcoes)

        TxtOrigem.insert(0,caminhoOrigem)
        

        #aqui seleciona a pasta a ser colocada o novo arquivo
        tkMessageBox.showinfo("Selecionar Pasta", message= "Selecione Pasta de Destino!")
        opcoes = {}                # as opções são definidas em um dicionário
        opcoes['initialdir'] = ''    # será o diretório atual
        opcoes['parent'] = tinicial
        opcoes['title'] = 'Selecione Pasta de destino!'
        caminhoFinal = fdlg.askdirectory(**opcoes)

        TxtDestino.insert(0,caminhoFinal)

        TxtDestino.config(state='disabled')
        TxtOrigem.config(state='disabled')
        # comboFormato.config(state='disabled')
        tinicial.update()

        
        removeBG.origem = caminhoOrigem
        removeBG.destino = caminhoFinal
        # chamando.formato ="." + comboFormato.get()

        if (removeBG.origem  and removeBG.destino):
            removeBG.ExecultaRemocao()
        else:
            tkMessageBox.showinfo("Erro Caminhos", message= "Verifique os caminhos!")
            sys.exit()
        # df.to_excel(caminhoFinal +'/'+ nomedoarquivo +"-"+ data_atual + '.xlsx', index=False)
        
        LblStatus.configure(text = "Finalizado")
        tkMessageBox.showinfo("Finalizado", message= "Finalizado verifique em: " + caminhoFinal)
        TxtDestino.config(state='normal')
        TxtOrigem.config(state='normal')
        # comboFormato.config(state='normal')
        TxtOrigem.delete(0,"end")
        TxtDestino.delete(0,"end")
    except :
        tkMessageBox.showinfo("Erro2", message= "Tente Novamente!")
        LblStatus.configure(text = "Tente novamente")
        TxtDestino.config(state='normal')
        TxtOrigem.config(state='normal')
        # comboFormato.config(state='normal')
        TxtOrigem.delete(0,"end")
        TxtDestino.delete(0,"end")
                
	


tinicial = tk.Tk()
tinicial.geometry("800x550+200+100")
tinicial.title("Remove BG")
tinicial.resizable(width=False, height=False)
tinicial['bg'] = 'black'
tinicial.iconphoto(True, PhotoImage(file='./arquivos/convert.png'))
image=PhotoImage(file='./arquivos/convert.png')

robozinho = Label(tinicial, image = image,width=780, height=440,bg ="white")
robozinho.grid(rowspan=10,columnspan =10,pady=10, padx=10)

cmdCadastrar=Button(tinicial,bd=10,bg = 'white',fg='black',text='Selecionar',font=('arial',12,'bold'),
	command = RemoveBG).grid(row=12,column=1)

LblOrigem=Label(tinicial,bd=4,bg = 'black',fg='white',text='Origem',font=('arial',10,'bold'),height=1).grid(row=11, column=3)
TxtOrigem=Entry(tinicial,bd=4,bg = 'white',fg='black',font=('arial',10,'bold'),width=50,)
TxtOrigem.grid(row=11, column=4)
# TxtOrigem.insert(0,"Relatorio-Excell")

LblDestino=Label(tinicial,bd=4,bg = 'black',fg='white',text='Destino',font=('arial',10,'bold'),height=1).grid(row=12, column=3)
TxtDestino=Entry(tinicial,bd=4,bg = 'white',fg='black',font=('arial',10,'bold'),width=50,)
TxtDestino.grid(row=12, column=4)

# LblFormato=Label(tinicial,bd=4,bg = 'Cornsilk',fg='black',text='Formato',font=('arial',10,'bold'),height=1).grid(row=11, column=5)
# comboFormato = ttk.Combobox(tinicial,width=9,values=["mp4","mkv"],font=('arial',10,'bold'))
# comboFormato.grid(row=12,column=5)
# comboFormato.current(0)

LblStatus=Label(tinicial,bd=4,bg = 'Cornsilk',fg='black',text='',font=('arial',10,'bold'),height=1)

tinicial.mainloop()



