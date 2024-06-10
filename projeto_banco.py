#Boas vindas
print ("Olá Usuário,")

#Menu principal
menu = '''
    ====== MENU ======

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

    ==================

Qual operação deseja realizar: '''

#Definindo variaveis
saldo = 0
LIMITE_SAQUE = 3
extrato = "Extrato:\n"
saque_maximo = 500
qtde_saque = 0


while True:

    operacao = input (menu)

    if operacao == "q":
        break
    elif operacao == "d":
        valor = float(input("Qual valor a depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f'Valor depositado: R$ {valor:.2f}\n'
            print (f'Valor depositado: R$ {valor:.2f}')
        else:
            print ("Valor inválido, por favor informe um valor acima de 0.")

    elif operacao == "e":
        print (extrato)
        print (f'Seu saldo é R$ {saldo:.2f}')
    elif operacao == "s":
        
        if qtde_saque < LIMITE_SAQUE:

            valor = float(input('Qual valor deseja sacar: '))
            
            if valor>0 and valor<=500 and saldo>=valor and qtde_saque <= LIMITE_SAQUE :
                saldo -= valor
                extrato += f'Valor sacado: R$ {valor:.2f}\n'
                qtde_saque += 1
            elif saldo < valor:
                print('Saldo insuficiente.')
            elif valor > 500:
                print ('Seu limite de saque máximo é R$ 500.')
            else:
                print('Valor invalido, por favor informe um valor avima de 0.')

        else:
            print('Você atingiu seu limite de saque diário.')