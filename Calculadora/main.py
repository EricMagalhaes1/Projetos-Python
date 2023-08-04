import tkinter as tk

calculo = ""

def add_calculo(sylbol):
    global calculo
    calculo += str(sylbol)
    texto_resultado.delete(1.0, "end")
    texto_resultado.insert(1.0, calculo)

def evaluate_calculo():
     global calculo
     try:
        print(calculo)
        calculo = str(eval(calculo))
        texto_resultado.delete(1.0, "end")
        texto_resultado.insert(1.0, calculo)
     except:
        limpa_campo()
        texto_resultado.insert(1.0, "Erro")

def limpa_campo():
    global calculo
    calculo = ""
    texto_resultado.delete(1.0, "end")


root = tk.Tk()
root.geometry('300x275')
root.maxsize(300, 275)


texto_resultado = tk.Text(root, height=2, width=16, font=('Arial', 24))
texto_resultado.grid(columnspan=5)

btn_1 = tk.Button(root, text='1', command=lambda: add_calculo(1), width=5, font=("Arial", 14))
btn_1.grid(row=2 ,column=1)
btn_2 = tk.Button(root, text='2', command=lambda: add_calculo(2), width=5, font=("Arial", 14))
btn_2.grid(row=2 ,column=2)
btn_3 = tk.Button(root, text='3', command=lambda: add_calculo(3), width=5, font=("Arial", 14))
btn_3.grid(row=2 ,column=3)
btn_4 = tk.Button(root, text='4', command=lambda: add_calculo(4), width=5, font=("Arial", 14))
btn_4.grid(row=3 ,column=1)
btn_5 = tk.Button(root, text='5', command=lambda: add_calculo(5), width=5, font=("Arial", 14))
btn_5.grid(row=3 ,column=2)
btn_6 = tk.Button(root, text='6', command=lambda: add_calculo(6), width=5, font=("Arial", 14))
btn_6.grid(row=3 ,column=3)
btn_7 = tk.Button(root, text='7', command=lambda: add_calculo(7), width=5, font=("Arial", 14))
btn_7.grid(row=4 ,column=1)
btn_8 = tk.Button(root, text='8', command=lambda: add_calculo(8), width=5, font=("Arial", 14))
btn_8.grid(row=4 ,column=2)
btn_9 = tk.Button(root, text='9', command=lambda: add_calculo(9), width=5, font=("Arial", 14))
btn_9.grid(row=4 ,column=3)
btn_0 = tk.Button(root, text='0', command=lambda: add_calculo(0), width=5, font=("Arial", 14))
btn_0.grid(row=5 ,column=2)
btn_mais = tk.Button(root, text='+', command=lambda: add_calculo("+"), width=5, font=("Arial", 14))
btn_mais.grid(row=2 ,column=4)
btn_menos = tk.Button(root, text='-', command=lambda: add_calculo('-'), width=5, font=("Arial", 14))
btn_menos.grid(row=3 ,column=4)
btn_vezes = tk.Button(root, text='*', command=lambda: add_calculo('*'), width=5, font=("Arial", 14))
btn_vezes.grid(row=4 ,column=4)
btn_div = tk.Button(root, text='/', command=lambda: add_calculo('/'), width=5, font=("Arial", 14))
btn_div.grid(row=5 ,column=4)
btn_abre = tk.Button(root, text='(', command=lambda: add_calculo('('), width=5, font=("Arial", 14))
btn_abre.grid(row=5 ,column=1)
btn_fecha = tk.Button(root, text=')', command=lambda: add_calculo(')'), width=5, font=("Arial", 14))
btn_fecha.grid(row=5 ,column=3)
btn_limpar = tk.Button(root, text='C', command=limpa_campo, width=11, font=("Arial", 14))
btn_limpar.grid(row=6 ,column=3, columnspan=2)
btn_igual = tk.Button(root, text='=', command=evaluate_calculo, width=11, font=("Arial", 14))
btn_igual.grid(row=6 ,column=1, columnspan=2)


root.mainloop()

