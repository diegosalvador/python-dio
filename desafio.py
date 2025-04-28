class Conta:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.historico = []  # Lista para armazenar o histórico de transações

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 500:
            print("Saque inválido. O limite por operação é de R$500,00.")
        elif 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saque inválido. Verifique o saldo ou o valor solicitado.")

    def extrato(self):
        print("\n=== Extrato ===")
        if self.historico:
            for transacao in self.historico:
                print(transacao)
        else:
            print("Nenhuma transação realizada.")
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("================\n")


def menu():
    conta = Conta()  # Cria uma conta com saldo inicial de 0
    while True:
        print("\n=== Menu ===")
        print("1. Depositar")
        print("2. Extrato")
        print("3. Sacar")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor = float(input("Digite o valor para depósito: "))
                conta.depositar(valor)
            except ValueError:
                print("Por favor, insira um valor numérico válido.")

        elif opcao == "2":
            conta.extrato()

        elif opcao == "3":
            try:
                valor = float(input("Digite o valor para saque: "))
                conta.sacar(valor)
            except ValueError:
                print("Por favor, insira um valor numérico válido.")

        elif opcao == "4":
            print("Encerrando o programa. Obrigado por usar nosso serviço!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    menu()