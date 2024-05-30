#IMPORTAÇÃO DE ALGUMAS BIBLIOTECAS
import colorama
from colorama import Fore, Back, Style
import time
from datetime import datetime as dt

#PARA DATA NO EXTRATO
data = dt.now()
Hora = 0
Minuto = 0
Segundo = 0
Hora = data.hour
Minuto = data.minute
Segundo = data.second
horadata = data.strftime("%d/%m/%y - %H:%M:%S")

#INÍCIO DO SISTEMA

menu = Fore.BLUE + '\nESCOLHA UMA OPÇÃO'+  Fore.GREEN + '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

>>>''' + Fore.RESET 

#VARIÁVEIS GERAIS

saldo = 0
limite = 1000
extrado = ''
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu).lower()
    
    if opcao == 'd':
        valor = float(input('Informe o valor a depositar: '))

        if valor > 0:
            saldo += valor
            extrado += f'Despósitos: R$ {valor:.2f} em {horadata}\n'
        else:
            print(Fore.BLACK + Back.RED + Style.NORMAL +'\nOperação falhou! O valor informado não é válido.'+ Fore.RESET +  Back.RESET + Style.RESET_ALL)
    
    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print(Fore.BLACK + Back.RED + Style.NORMAL +'\nVocê Não possui saldo suficiente!' + Fore.RESET +  Back.RESET + Style.RESET_ALL)

        elif excedeu_limite:
            print('limite Insuciente')
        
        elif excedeu_saques:
            print('Número de saques excedido')
        
        elif valor > 0:
            saldo -= valor
            extrado += f'Saque: R$ {valor:.2f} em {horadata}\n'
            numero_saques += 1
        
        else:
            print(Fore.BLACK + Back.RED + Style.NORMAL +'\nOperação falhou! O valor informado não é válido.'+ Fore.RESET +  Back.RESET + Style.RESET_ALL)

    elif opcao == 'e':
        print(Fore.BLUE + Back.LIGHTWHITE_EX +'\n============EXTRATO============' + Fore.RESET + Back.RESET)
        print('\nNão oram realizadas movimentações.' if not extrado else extrado)
        print(f'\nSaldo de: R$ {saldo:.2f}')
        print(Fore.BLUE + Back.LIGHTWHITE_EX + '============FIM============' + Fore.RESET + Back.RESET)


    elif opcao == 'q':
        break

    else:
        print(Fore.BLACK + Back.RED  +'\nOperação falhou! O valor informado não é válido.'+ Fore.RESET +  Back.RESET )


#fim do desafio