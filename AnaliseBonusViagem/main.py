import pandas as pd
from twilio.rest import Client

account_sid = "ACf15f767a4a0c1cff6f3748e06156a95b"

auth_token = "5f81832d5a78c2e552f7c029d7486252"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mes de {mes} alguem bateu a meta. Vendedor: {vendedor} , Vendas: R${vendas}')
        message = client.messages.create(
            to="+5531999934744",
            from_="+16  672398756",
            body=f'No mes de {mes} alguem bateu a meta. Vendedor: {vendedor} , Vendas: R${vendas}')
        print(message.sid)
