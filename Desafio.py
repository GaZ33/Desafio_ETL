import pandas as pd
from colorama import init, Fore, Back, Style

# Função principal, é o menu do banco
def main():

    # Ler o arquivo CSV para um DataFrame
    df = pd.read_csv("planilha_dados.csv", index_col="cpf")
    df.index = df.index.astype(str)
    # Converter o DataFrame de volta para um dicionário
    usuarios = df.to_dict(orient="index")

    while True:
        menu_menu()
        #Entrada de opções, decidirá qual raiz o user seguirá
        opcao = input(f"{Fore.RED}").lower()
        if opcao == "s":
            print(Fore.RED + "Saindo...")
            # Converter o dicionário para um DataFrame do Pandas
            df = pd.DataFrame.from_dict(usuarios, orient="index")

            # Escrever o DataFrame em um arquivo CSV
            df.to_csv("planilha_dados.csv", index_label="cpf")
            break

        elif opcao == "nu":
            criar_usuário(usuarios)

        elif opcao == "en":
            entrar(usuarios)

        else:
            print(f"""{Fore.RED}Operação inválida. 
{Fore.WHITE}Por favor selecione novamente uma operação.""")


def menu_menu():
    print(f"""{Fore.GREEN}==============================
    {Fore.BLUE}[nu] Criar usuário
    {Fore.GREEN}[en] Entrar
    {Fore.RED}[s] Sair{Fore.GREEN}
=============================={Fore.BLACK}""")

def agencias():
    print(f"""[1] Agência 3885 - Av. Rui Barbosa
[2] Agência 0041 - R. Moraes Barros
[3] Agência 3246 - R. Moraes Barros""")


def menu_logado():
    print(f"""
    {Fore.GREEN}=======================================
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
            if quantidade > float(usuarios[cpf]["valor"]) :
                print("Operação inválida, saldo indisponível")
            
            else:
                usuarios[cpf]["valor"] = usuarios[cpf]["valor"] - quantidade 
                usuarios[cpf]["extrato"] += f'Saque R$ {quantidade:.2f}\n'

        elif opcao_logado == "2":
            quantidade = float(input("Digite o valor que deseja depositar: "))
            usuarios[cpf]["valor"] = quantidade + usuarios[cpf]["valor"]
            usuarios[cpf]["extrato"] += f'Deposito R$ {quantidade:.2f}\n'

        elif opcao_logado == "3":
            print(usuarios[cpf]["extrato"])
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
        cpf = input(f"""=======================================
    Informe o CPF do usuário
Caso queira sair desse menu digite 0 
=======================================
""")
        if cpf == '0':
            break
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
                        {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "agencia": agencia,
                        "valor": 0, "extrato": ""}
                        })
        print("=== Usuário criado com sucesso! ===")
        break


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = cpf in usuarios
    return usuarios_filtrados

main()