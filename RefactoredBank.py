import textwrap

class Cliente:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class Conta:
    def __init__(self, agencia, numero_conta, cliente):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.cliente = cliente

def criar_cliente():
    cpf = input("Informe o CPF (somente números): ")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    return Cliente(cpf, nome, data_nascimento, endereco)

def criar_conta(cliente):
    agencia = "0001"
    numero_conta = len(contas) + 1
    return Conta(agencia, numero_conta, cliente)

def listar_contas():
    for conta in contas:
        print("=" * 100)
        print(f"Agência:\t{conta.agencia}")
        print(f"C/C:\t\t{conta.numero_conta}")
        print(f"Titular:\t{conta.cliente.nome}")

def menu():
    print("\n=== MENU ===")
    print("d - Depositar")
    print("s - Sacar")
    print("e - Exibir extrato")
    print("nu - Novo usuário")
    print("nc - Nova conta")
    print("lc - Listar contas")
    print("q - Sair")
    return input("Escolha uma opção: ").lower()

def main():
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo += valor
            extrato += f"Depósito: + R${valor}\n"

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            if saldo - valor >= 0 and numero_saques < LIMITE_SAQUES:
                saldo -= valor
                extrato += f"Saque: - R${valor}\n"
                numero_saques += 1
            else:
                print("Operação inválida. Saldo insuficiente ou limite de saques atingido.")

        elif opcao == "e":
            print(f"Saldo: R${saldo}")
            print("Extrato:")
            print(extrato)

        elif opcao == "nu":
            cliente = criar_cliente()
            clientes.append(cliente)
            print("=== Cliente criado com sucesso! ===")

        elif opcao == "nc":
            cliente = criar_cliente()
            conta = criar_conta(cliente)
            contas.append(conta)
            print("=== Conta criada com sucesso! ===")

        elif opcao == "lc":
            listar_contas()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

clientes = []
contas = []
main()
