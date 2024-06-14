menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuario
[c] Criar conta
[l] Listar contas
[q] Sair

=> """

def deposito (saldo, valor, extrato):
    saldo += valor
    extrato += f"Depósito: R${valor:.2f}\n"
    print(f"Valor depositado: R${valor:.2f}")

    return saldo, extrato

def saque (saldo, valor, extrato, saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Você atingiu o limite de saques.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        saques += 1
        print(f"Valor sacado: R${valor:.2f}")
    else:
        print("O valor informado é inválido.")

    return saldo, extrato, saques

def exibir_extrato (extrato, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("==========================================")
    
def verificar_validade_cpf (cpf):
    for letter in cpf:
        if letter != "1" and letter != "2" and letter != "3" and letter != "4" and letter != "5" and letter != "6" and letter != "7" and letter != "8" and letter != "9" and letter != "0":
            return False
    
    return True

def criar_usuario (usuarios):
    while True:
        cpf = input("Digite seu CPF (somente números): ")
        if cpf == "q" or cpf == "Q":
            return
        elif verificar_validade_cpf(cpf) == False:
            print("CPF inválido.\n[q] Sair.")
        else:
            break
    if checar_cpf(cpf) == False:
        return
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aa): ")
    endereco = definindo_endereco()
    usuarios.append({"nome": nome, 
                     "CPF": cpf, 
                     "data_nascimento": data_nascimento,
                     "endereco": endereco})

def definindo_endereco ():
    endereco = ""
    endereco += input("Logradouro: ") + ", "
    endereco += input("Número: ") + " - "
    endereco += input("Bairro: ") + " - "
    endereco += input("Cidade: ") + "/"
    endereco += input("Estado (sigla): ")

    return endereco

def checar_cpf (cpf):
    
    for usuario in usuarios:
        if  usuario["CPF"] == cpf:
            print ("CPF já cadastrado.")
            return False
    return

def criar_conta(agencia, numero_conta, usuarios):
    while True:
        cpf = input("Qual CPF do usuário: ")
        if cpf == "q" or cpf == "Q":
            return
        elif verificar_validade_cpf(cpf) == False:
            print("CPF inválido.\n[q] Sair.")
        else:
            break
    if type(checar_cpf_conta(cpf)) == type(""):
        usuario = checar_cpf_conta(cpf)
        print("Conta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não cadastrado.")
        return
        
def checar_cpf_conta (cpf):
    for i in usuarios:
        if i["CPF"] == cpf:
            return i["nome"]
    return False

AGENCIA = "0001"
contas = []
usuarios = []    
saldo = 0
limite = 500
extrato = ""
saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo, extrato = deposito(saldo, valor, extrato)
        else:
            print("O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato, saques = saque(saldo, valor, extrato, saques)

    elif opcao == "e":
        exibir_extrato(extrato, saldo)

    elif opcao == "u":
        criar_usuario(usuarios)

    elif opcao == "l":
        print(contas)
    
    elif opcao == "c":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")