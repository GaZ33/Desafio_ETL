#import pandas as pd

#df = pd.read_csv('planilha_dados.csv')
#print(df)

# Função principal, é o menu do banco
def main():
    usuarios = {}
    #contas = []
    while True:
        menu_menu()
        #Entrada de opções, decidirá qual raiz o user seguirá
        opcao = input().lower()
        if opcao == "s":
            print("Saindo...")
            break

        elif opcao == "nu":
            criar_usuário(usuarios)

        elif opcao == "en":
            entrar(usuarios)

        else:
            print("Operação inválida. Por favor selecione novamente uma operação.")


def menu_entrar():
    print(f"""
    ==============================
            Digite seu CPF
    ==============================
    """)
    ...


def menu_menu():
    print(f"""==============================
    [nu] Criar usuário
    [en] Entrar
    [s] Sair
==============================""")

def agencias():
    print(f"""[1] Agência 3885 - Av. Rui Barbosa
    [2] Agência 0041 - R. Moraes Barros
    [3] Agência 3246 - R. Moraes Barros""")


def menu_logado():
    print(f"""
    =======================================
    [1] Sacar
    [2] Depositar
    [3] Extrato
    [4] Sair para entrar com outro CPF
    [5] Voltar ao menu inicial
    =======================================
    """)


def logado(cpf, usuarios):
    logado = 2
    while logado == 2:
        menu_logado()
        opcao_logado = input()
        if opcao_logado == "1":
            quantidade = float(input("Digite o valor que deseja sacar: "))
            if quantidade > usuarios["cpf"]["valor"]:
                print("Operação inválida, saldo indisponível")
            
            else:
                usuarios["cpf"]["valor"] -= quantidade
                usuarios["cpf"]["extrato"] += f'Saque R$ {quantidade:.2f}\n'

        elif opcao_logado == "2":
            quantidade = float(input("Digite o valor que deseja depositar: "))
            usuarios["cpf"]["valor"] += quantidade
            usuarios["cpf"]["extrato"] += f'Saque R$ {quantidade:.2f}\n'

        elif opcao_logado == "3":
            print(usuarios["cpf"]["extrato"])
        elif opcao_logado == "4":
            print("Saindo...")
            return 1
        elif opcao_logado == "5":
            print("Saindo...")
            return 0
        else:
            print("Operação inválida. Por favor selecione novamente uma operação.")

def entrar(usuarios):
    entrar = 1
    while entrar == 1:
        menu_entrar()
        cpf = input("Informe o CPF do usuário: ")
        if filtrar_usuario(cpf, usuarios):
            entrar = logado(cpf, usuarios)
        else:
            print(f"""=======================================
    CPF inserido não cadastrado 
        Voltando para o menu...
=======================================
""")
            entrar = 0


def criar_usuário(usuarios):
    while True:
        cpf = input(f"""=======================================
            Digite seu CPF
Caso queira sair desse menu digite 0 
=======================================
""")
        if cpf == '0':
            break

        usuario = filtrar_usuario(cpf, usuarios)

        # Verificadno se há uma conta com esse CPF
        if usuario:
            print("\nJá existe um usuário com esse CPF.")
            continue
            
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        #op = True
        # Escolha de agência
        while True:
            agencias()
            opcao = input("Escolha uma agência: ")
            if opcao == '1':
                agencia = "3885"
                break
            elif opcao == '2':
                agencia = "0041"
                break
            elif opcao == '3':
                agencia = "3246"
                break
            else:
                print("Opção inválida, digite novamente\n")
        # Adiciona um dicionário vazio no dicionário usuários para o CPF inserido
        usuarios.setdefault(cpf, {})
        # Colocando os dados que foram iseridos no dicionário com a chave CPF
        usuarios.update({cpf:
                        {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco, "agencia": agencia,
                        "valor": 0, "extrato": ""}
                        })
        print("=== Usuário criado com sucesso! ===")
        break


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = cpf in usuarios
    return usuarios_filtrados


#def criar_conta(numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

main()