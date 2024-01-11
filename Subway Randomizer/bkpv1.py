import random as rd
import pandas as pd
import os
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('SubwayRandomizer')
root.geometry('600x320')
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background='#1d1d1d')

sauce_amt = rd.randint(1, 4)
salad_amt = rd.randint(1, 9)



def get_bread():
    bread_selector = rd.randint(1, 4)
    table_bread = pd.read_excel('Breads.xlsx')
    bread = table_bread.loc[table_bread['Code'] == bread_selector, 'Bread'].values[0]
    return bread


def get_flavor():
    flavor_selector = rd.randint(1, 9)
    table_flavor = pd.read_excel('Flavors.xlsx')
    flavor = table_flavor.loc[table_flavor['Code'] == flavor_selector, 'Flavor'].values[0]
    return flavor


def get_cheese():
    cheese_selector = rd.randint(1, 3)
    table_cheese = pd.read_excel('Cheese.xlsx')
    cheese = table_cheese.loc[table_cheese['Code'] == cheese_selector, 'Cheese'].values[0]
    return cheese


def get_salad():
    table_salad = pd.read_excel('Salads.xlsx')
    sauce = table_salad.loc[table_salad['Code'] == salad_selector, 'Salad'].values[0]
    return sauce


def get_sauce():
    table_sauces = pd.read_excel('Sauces.xlsx')
    sauce = table_sauces.loc[table_sauces['Code'] == sauce_selector, 'Sauce'].values[0]
    return sauce


while sauce_amt > 0:
    sauce_picker = rd.sample(range(1, 9), sauce_amt)
    sauce_list = []
    for sauces in sauce_picker:
        sauce_selector = sauces
        get_sauce()
        sauce_list.append(get_sauce())
        sauce_amt = sauce_amt - 1

while salad_amt > 0:
    salad_picker = rd.sample(range(1, 7), salad_amt)
    salad_list = []
    for salad in salad_picker:
        salad_selector = salad
        get_salad()
        salad_list.append(get_salad())
        salad_amt = salad_amt - 1


message = f'''-------------------------------------------------------------
Pão:
{get_bread()}
-------------------------------------------------------------
Recheio:
{get_flavor()}
-------------------------------------------------------------
Queijo:
{get_cheese()}
-------------------------------------------------------------
Saladas:
{', '.join(salad_list)}
-------------------------------------------------------------
Molhos:
{', '.join(sauce_list)}
'''

message1 = Label(root, bg='#1d1d1d', fg='#FFFFFF', font=('Montserrat', 12, 'bold'))
message1.config(text=message)
message1.pack()

tela = tk.Canvas(root, width=600, height=60, bg='#1d1d1d', highlightthickness=0, relief='ridge')

root.mainloop()
