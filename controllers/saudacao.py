from datetime import datetime
from time import sleep

def saudacao():
    hora = datetime.now(tz=None)

    if hora.hour >= 5 and hora.hour < 13:
        print("bom dia")
    if hora.hour >=13 and hora.hour <18:
        print("boa tarde")
    else:
        print(" boa noite ")

def cabesalho():
    
    poli = "="*20

    for i in range(10):
        sleep(0.1)
        print("*")
    print(poli,"seja bem vindo ao blucarros!!!",poli)
    print(poli, "Sua Plataforma de Compra e Venda de Carros Nacionais",poli)

def descritivo():
    print()
    print("as opções abaixo represantam as suas possibilidades de escolha")
    print('''
1- anuciar
2- comprar 
3- consultar fipe
          ''')


