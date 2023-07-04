from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "b37d90aad3f5f24a6c60"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())
    data.sort()
    
    return data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol","")
        print(f"{_id} - {name} - {symbol}")


def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    if len(data) == 0:
        print('Moedas Invalidas.')
        return

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")

    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Quantidade Invalida.")
        return
    
    converted_amount = rate * amount
    print(f"{amount} {currency1} é igual a {converted_amount} {currency2}")
    return converted_amount 

def main():
    currencies = get_currencies()
    print("""\n
===================== MENU =====================
Bem Vindo ao conversor de moedas!
Lista - listar as diferentes moedas
Converter - converter de uma moeda para outra
Rate - mostra a proporção entre as duas moedas \n
    """)

    while True:
        command = input("Insira o comando que deseja (pressione 'q' para sair): ").lower()
        
        if command == "q":
            break
        elif command =="lista":
            print_currencies(currencies)
        elif command == "converter":
            currency1 = input("Digite o ID da moeda que será convertida: ").upper()
            amount = input(f"Digite a quantidade em {currency1} que você deseja converter: ").upper()
            currency2 = input("Digite o ID da moeda que deseja converter: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Digite o ID da moeda que será convertida: ").upper()
            currency2 = input("Digite o ID da moeda que deseja converter: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Comando Invalido!")

main()
