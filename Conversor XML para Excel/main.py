import xmltodict as xd
import os

def pegar_info(nome_arquivo):
    print(f'Pegou as Informacoes {nome_arquivo}')
    with open (f'nfs/{nome_arquivo}', 'rb') as arquivo_xml:
        dic_arquivo = xd.parse(arquivo_xml)
        print(dic_arquivo)

listar_arquivos = os.listdir

for arquivos in listar_arquivos:
    pegar_info(arquivos)
    break
