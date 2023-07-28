import pandas as  pd
import os

if('df_despesas.cvs' in os.listdir()) and ('df_receitas.csv' in os.listdir()):
    df_despesas = pd.read_csv('df_despesas.cvs', index_col=0, parse_dates=True)
    df_receitas = pd.read_csv('df_receitas.cvs', index_col=0, parse_dates=True)

else:
    data_structure = {'Valor':[],
        'Efetuado':[],
        "Fixo": [],
        'Data':[],
        'Categoria':[],
        'Descrição':[],}
    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_receitas.to_csv('df_receitas.csv')
    df_despesas.to_csv('df_despesas.csv')


if('df_cat_despesas.cvs' in os.listdir()) and ('df_cat_receitas.csv' in os.listdir()):
    df_cat_receitas = pd.read_csv('df_cat_receitas.cvs', index_col=0)
    df_cat_receitas = pd.read_csv('df_cat_receitas.cvs', index_col=0)

else:
    cat_receitas = {'Categorias': ['Salário','Investimentos', 'Comissão']}
    cat_despesas ={'Categorias':['Alimentação', 'Aluguel', 'Gasolina', 'Saúde', 'Lazer']}

    df_cat_receitas = pd.DataFrame(cat_receitas)
    df_cat_despesas = pd.DataFrame(cat_despesas)
    df_cat_receitas.to_csv('df_cat_receitas.csv')
    df_cat_despesas.to_csv('df_cat_despesas.csv')


