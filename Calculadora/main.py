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

root.mainloop()

