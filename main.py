import datetime
data = datetime.datetime.now()

numero_conta = 0

class Banco:
    def __init__(self):
        self.clientes = []
    
    def criar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def mostrar_clientes(self):
        if not self.clientes:
            print("Não existem clientes cadastrados")
        else:
            print("Lista de Clientes:")
            for cliente in self.clientes:
                print(cliente)   
    
    def verificar_cpf(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None
    
    def verificar_num_conta(self, cpf, numero_conta):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                for conta in cliente.contas:
                    if conta.numero_conta == numero_conta:
                        return conta
        return None
        
    
    def dados_do_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente.nome, cliente.data_nascimento, cliente.telefone, cliente.endereco
        
class Cliente:
    def __init__(self, nome, data_nascimento, cpf , telefone, endereco):
        self.contas = []
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        
    def criar_conta(self, conta):
        self.contas.append(conta)

    
    
    #escrever na lista os dados
    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"Data de Nascimento: {self.data_nascimento}\n"
                f"CPF: {self.cpf}\n"
                f"Telefone: {self.telefone}\n"
                f"Endereço: {self.endereco}\n")
                
banco = Banco()

class Conta:
    def __init__(self, numero_conta, saldo, tipo, numero_agencia):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.tipo = tipo
        self.numero_agencia = numero_agencia
        self.extrato_conta = []
        self.contador_extrato = 0
        
    def __str__(self):
        return (f"N° da Conta: {self.numero_conta}\n"
                f"N° da Agência: {self.numero_agencia}\n")
    
    def depositar(self):
        valor_deposito = input("Digite o valor do depósito\n=> ")
        if valor_deposito.isnumeric() and float(valor_deposito) > 0:
            self.saldo += float(valor_deposito)
            self.contador_extrato += 1
            self.extrato_conta.append(f"{self.contador_extrato}. Depósito de R${'%.2f' % float(valor_deposito)} - {data.strftime("%d/%m/%Y")}")
            print("="*40)
            print(f"Depósito Concluído de R${'%.2f' % float(valor_deposito)}")
            print("="*40)
        else:
            print("="*40)
            print("Valor inválido para depósito.")
            print("="*40)
            
    def sacar(self):
        valor_saque = input("Digite o valor do saque\n=> ")
        if valor_saque.isnumeric():
            vlr_saque = float(valor_saque)
            if vlr_saque <= self.saldo:
                self.saldo -= vlr_saque
                self.contador_extrato += 1
                self.extrato_conta.append(f"{self.contador_extrato}. Depósito de R${'%.2f' % vlr_saque} - {data.strftime("%d/%m/%Y")}")
                print("="*40)
                print(f"Saque Concluído de R${'%.2f' % vlr_saque}")
                print("="*40)
            else:
                print("="*40)
                print("Saldo Insuficiente")
                print("="*40)
        else:
            print("="*40)
            print("Valor inválido para saque.")
            print("="*40)
        
    def extrato(self):
        for transacao in self.extrato_conta:
            print(transacao)
        
    def transferir(self):
        #perguntar qual o numero da conta que quer fazer a transferência
        conta_destino_cpf = input("Digite o CPF da conta de destino\n=> ")
        conta_destino_num = input("Digite o N° da conta de destino\n=> ")
        conta_destino = banco.verificar_num_conta(cpf=conta_destino_cpf, numero_conta=int(conta_destino_num))
        if conta_destino is not None:
            valor_transferencia = input("Digite o valor da transferência\n=> ")
            self.saldo -= float(valor_transferencia)
            conta_destino.saldo += float(valor_transferencia)
            self.contador_extrato += 1
            self.extrato_conta.append(f"{self.contador_extrato}. Transferência de R${'%.2f' % float(valor_transferencia)} - {data.strftime("%d/%m/%Y")}")
            print(f"Transferência Côncluida no valor de R${'%.2f' % float(valor_transferencia)}")
        else:
            print("Conta não existe!")

def calcular_idade(data_nascimento):
    hoje = datetime.datetime.today()
    # Converte a data de nascimento em um objeto datetime
    data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
    # Calcula a diferença de anos
    idade = hoje.year - data_nascimento.year
    # Verifica se ainda não fez aniversário este ano
    if hoje.month < data_nascimento.month or (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
        idade -= 1
    return idade

def novo_cliente(cpf):
    while True:
        nome = input("Digite seu nome:\n=> ")
        if nome.isalpha():
            data_nascimento = input("Digite sua data de nascimento:\n=> ")
            data_valida = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
            if data_valida:
                idade = calcular_idade(data_nascimento)
                telefone = input("Digite seu telefone:\n=> ")
                if len(telefone) == 9 or len(telefone) == 11 or len(telefone) == 13:
                    endereco = input("Digite seu endereço:\n=> ")
                    cliente = Cliente(nome, data_nascimento, cpf, telefone, endereco)
                    banco.criar_cliente(cliente)
                    print("="*40)
                    print("!","Novo cliente:".ljust(36),"!")
                    print("!                            !")
                    print("!",f"Nome: {nome}".ljust(36),"!")
                    print("!",f"Idade: {idade}".ljust(36),"!")
                    print("!",f"CPF: {cpf}".ljust(36),"!")         
                    print("!",f"Telefone: {telefone}".ljust(36),"!")
                    print("!",f"Endereço: {endereco}".ljust(36),"!")       
                    print("="*40)
                    break

                else:
                    print("="*40)
                    print("Telefone inexistente!")
                    print("="*40)
            else:
                print("="*40)
                print("INVÁLIDO!")
                print("Formata da data: dd/mm/aaaa")
                print("="*40)
        else:
            print("="*40)
            print("INVÁLIDO!")
            print("Digite apenas caracteres para o nome!")
            print("="*40)
        
def nova_conta(numero_conta, cpf):
    clientes = banco.verificar_cpf(cpf)
    numero_conta = int(numero_conta) + 1
    saldo = 0
    tipo = "Corrente"
    numero_agencia = "0001"
    conta_criada = Conta(numero_conta, saldo, tipo, numero_agencia)
    clientes.criar_conta(conta_criada)
    print("="*40)
    print("!","Nova conta:".ljust(36),"!")
    print("!                            !")
    print("!",f"N° da Conta: {numero_conta}".ljust(36),"!")
    print("!",f"N° da Agência: {numero_agencia}".ljust(36),"!")
    print("!",f"Tipo da Conta: {tipo}".ljust(36),"!")     
    print("="*40)
    return numero_conta

def menu(numero_conta, cliente, conta):
    while True:
        print("="*40)
        print("!",f"Conta N°{numero_conta}: de {cliente.nome}".ljust(36),"!")
        print("!                            !")
        print("!",f"Saldo: R${conta.saldo}".ljust(36),"!")
        print("!                            !")
        print("!","[1] Depositar".ljust(36),"!")
        print("!","[2] Sacar".ljust(36),"!")
        print("!","[3] Transferência".ljust(36),"!")    
        print("!","[4] Extrato".ljust(36),"!")    
        print("!","[5] Sair".ljust(36),"!")    
        print("="*40)
        opcao_menu_conta = input("Sua escolha:\n=> ")
        if opcao_menu_conta.isnumeric() and int(opcao_menu_conta) > 0 and int(opcao_menu_conta) <= 5:
            opcao_escolhida_conta = int(opcao_menu_conta)
            if opcao_escolhida_conta == 1:
                conta.depositar()
            elif opcao_escolhida_conta == 2:
                conta.sacar()
            elif opcao_escolhida_conta == 3:
                conta.transferir()
            elif opcao_escolhida_conta == 4:
                print("-"*36)
                print("!",f"Extrato de {cliente.nome}".center(36),"!")
                print("-"*36)
                conta.extrato()
                print(f"Saldo atual: R${'%.2f' % conta.saldo}".ljust(36))
                print("="*40)
            elif opcao_escolhida_conta == 5:
                break
    
# Menu - Enquanto não escolher a 3° opção continua em loop
while True:
    print("="*40)
    print("!","GuiBank".center(36),"!")
    print("="*40)
    print("!","Seja Bem Vindo ao GuiBank!".center(36),"!")
    print("="*40)
    print("""! Escolha uma opção:                   !
!                                      !
! [1] Login                            !
! [2] Nova Conta                       !
! [3] Sair                             !
========================================""")
# Verifica se opcão é valida
# Escolhas - opção escolhida é transformada em int
    opcao_menu = input("Sua escolha:\n=> ")
    if opcao_menu.isnumeric() and int(opcao_menu) > 0 and int(opcao_menu) <= 3:
        opcao_escolhida = int(opcao_menu)
        if opcao_escolhida == 1:
            cpf = input("Digite seu CPF:\n=> ")
            if cpf.isnumeric() and len(cpf) == 11:
                cliente = banco.verificar_cpf(cpf)
                print(cliente)
                if not cliente: 
                    print("Parece que você ainda não é nosso cliente, crie uma conta!")
                else:
                    numero_conta = input("Digite o numero da conta:\n=> ")
                    conta = banco.verificar_num_conta(cpf, int(numero_conta))
                    if not conta:
                        print(f"Conta N°{numero_conta} não existe, ou não pertence ao CPF{cpf}")
                    else:
                        menu(numero_conta, cliente, conta)
            else:
                print("="*40)
                print("CPF inválido")
                print("="*40)

        elif opcao_escolhida == 2:
            cpf = input("Digite seu CPF:\n=> ")
            if cpf.isnumeric() and len(cpf) == 11:
                cliente = banco.verificar_cpf(cpf)
                if not cliente: 
                    novo_cliente(cpf)
                    numero_conta = nova_conta(numero_conta,cpf)
                else:
                    numero_conta = nova_conta(numero_conta,cpf)
            else:
                print("="*40)
                print("CPF inválido")
                print("="*40)
        elif opcao_escolhida == 3:
            print("Programa Finalizado!")
            break
    else:
        print("""
OPÇÃO INVALIDA! TENTE NOVAMENTE.
              """)
