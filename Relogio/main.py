import tkinter as tk
from tkinter import *
import os
from time import strftime


root = tk.Tk()
root.title('Seu relogio')
root.geometry('600x320')
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background = '#1d1d1d')

def get_message():
    nome_usuario = os.getlogin()
    message.config(text='Olá ' + nome_usuario)

def get_data():
    data_atual = strftime(' %a, %d %b %Y')
    data.config(text= data_atual)

def get_horas():
    horas_atual = strftime('%H:%M:%S')
    horas.config(text = horas_atual)


tela = tk.Canvas(root, width=600, height=60, bg='#1d1d1d', highlightthickness=0, relief='ridge')
tela.pack()

message =  Label(root, bg='#1d1d1d',fg='#8e27ea', font=('Montserrat', 16))
message.pack()

data = Label(root, bg='#1d1d1d',fg='#8e27ea', font=('Montserrat', 14))
data.pack(pady=2)

horas = Label(root, bg='#1d1d1d',fg='#8e27ea', font=('Montserrat', 60, 'bold' ))
horas.pack(pady=2)


get_message()
get_data()
get_horas()

root.mainloop()
