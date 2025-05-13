import json
import os

Tudo = 'Tudo.json'
none_usuario = "Usuário não encontrado."
def carregar_dados():
    if os.path.isfile(Tudo):
        try:
            with open(Tudo, 'r') as f:
                Tudo = json.load(f)
                nomes = Tudo.get("nomes", [])
                senhas = Tudo.get("senhas", [])
                saldo_PYbucks = Tudo.get("saldo_PYbucks", [])
                pet_chapeu = Tudo.get("pet_chapeu", [])
                return nomes, senhas, pet_chapeu, saldo_PYbucks
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de dados. Inicializando base vazia.")
            return [], []
def salvar_dados(nomes, senhas):
    with open(Tudo, 'w') as f:
        json.dump({"nomes": nomes, "senhas": senhas}, f, indent=2)
#========================================================================================================================================================================================
#========================================================================================================================================================================================
nomes = []
senhas = []
saldo_PYbucks = []
pet_chapeu = []
nome_contacriar = ""
senha_contacriar = ""
acessarconta = ""
acessarcontabool = 0
senha = ""
senhabool = 0
areyousure = ""
GUI = 0
novo_nome = "" 
nova_senha = ""
chapeu = 0
#========================================================================================================================================================================================
#========================================================================================================================================================================================
def calvo():
    print("       ________________________________")
    print("      |                                |")
    print("      |                                |")
    print("      |      ____________________      |")
    print("      |     |                    |     |")
    print("      |     |                    |     |")


def chapeu_mexicano():
    print("       ________________________________")
    print("      |                                |")
    print("      |        ________________        |")
    print("      |  _____/________________\_____  |")
    print("      | \____________________________/ |")
    print("      |     |                    |     |")  


def chapeu_cartola():
    print("       ________________________________")
    print("      |         ______________         |")
    print("      |        |              |        |")
    print("      |        |              |        |")
    print("      |     ___|==============|___     |")
    print("      |    |______________________|    |")
    print("      |     |                    |     |")


def orelhas_gato():
    print("       ________________________________")
    print("      |        |\            /|        |")
    print("      |        | \          / |        |")
    print("      |      __|  \________/  |__      |")
    print("      |     |                    |     |")
    print("      |     |                    |     |")


def chapeu_crianca():
    print("       ________________________________")
    print("      |         -------T-------        |")
    print("      |         ,''''''|''''',         |")
    print("      |      __/_________ ____\__      |")
    print("      |     |                    |     |")
    print("      |     |                    |     |")


def pet_feliz():
    print("      |     |                    |     |")
    print("      |     |                    |     |")
    print("      |     |   0            0   |     |")
    print("      |_____|                    |_____|")
    print("     /      |  '--------------'  |      \ ")
    print("    /       |                    |       \ ")
    print("   /        |____________________|        \ ")
    print("  /                                        \ ")
    print(" /                                          \ ")
    print("/                                            \ ")

#========================================================================================================================================================================================
#========================================================================================================================================================================================
def sistema_base(nomes, senhas):
 while True:
    acessarcontabool = 0
    senhabool = 0
    acessar_conta = ""
    senha = "" 
    print("Bem vindo ao PYmagochi, oque deseja?")
    print("Insira 1 para criar uma conta")
    print("Insira 2 para listar todas as contas")
    print("Insira 3 para consultar o saldo da sua conta") 
    print("Insira 4 para observar o Pet da conta")
    print("Insira 5 para DELETAR a conta") 
    print("Insira 6 para alterar os valores da conta (senha e nome)") 
    print("Insira 7 para alterar o seu Pet") 
    print("Insira 8 para sair")
    escolhasistemabase =  input("Escreva a opção desejada: ")
    escolhasistemabase = int(escolhasistemabase)
    if escolhasistemabase ==1:
        criar_conta(nomes, senhas)
    elif escolhasistemabase ==2:
        listar_contas(nomes)
    elif escolhasistemabase ==3:
        consultar_conta(nomes, senhas, saldo_PYbucks)
    elif escolhasistemabase ==4:
        observar_pet(nomes, senhas, chapeu)
    elif escolhasistemabase ==5:
        DELETAR_conta(nomes, senhas, saldo_PYbucks)
    elif escolhasistemabase ==6:
        alterar_conta(nomes, senhas)
    elif escolhasistemabase ==7:
        alterar_pet(nomes, senhas, chapeu)
    elif escolhasistemabase ==8:
        break
#========================================================================================================================================================================================
#========================================================================================================================================================================================     
def criar_conta(nomes, senhas):
    nome_contacriar = input("Qual será o nome da sua conta? (você irá começar com 100 PYbucks!) ")
    nomes.append(nome_contacriar)
    senha_contacriar = input("Qual será a senha da sua conta? ")
    senhas.append(senha_contacriar)
    saldo_PYbucks.append(100)
    pet_chapeu.append(0)
    print("Sua conta "+nome_contacriar+ " foi criada com sucesso!")
    print("")
#========================================================================================================================================================================================
#========================================================================================================================================================================================
def acessar_conta(nomes, senhas, acessarcontabool, senhabool):
    acessar_conta = input("digite o nome da sua conta ")
    if acessar_conta in nomes:
        acessarcontabool = 1
    senha = input("digite a senha da sua conta ")
    if senha in senhas:
        senhabool = 1
    if acessarcontabool == 1 and senhabool == 1:
        print("")
    else:
        print("ERRO!! a senha ou o nome da conta estão errados!")  
        print("")
#========================================================================================================================================================================================
#========================================================================================================================================================================================
def listar_contas(nomes):
    for i in range(len(nomes)):
        print(nomes[i])
    print("")
#========================================================================================================================================================================================
#========================================================================================================================================================================================
def consultar_conta(nomes, senhas, saldo_PYbucks):
    acessar_conta = input("Digite o nome da sua conta: ")
    if acessar_conta in nomes:
        index = nomes.index(acessar_conta)  
        senha = input("Digite a senha da sua conta: ")
        if senhas[index] == senha:  
            print("Dados da sua conta: ")
            print("Nome: " + acessar_conta)
            print("Senha: " + senha)  
            print("Saldo: " + str(saldo_PYbucks[index]) + " PY$")
            print("")
        else:
            print("ERRO!! A senha está errada!")
            print("")
    else:
        print("ERRO!! O nome da conta não foi encontrado!")
        print("")
#========================================================================================================================================================================================
#========================================================================================================================================================================================
def DELETAR_conta(nomes, senhas, saldo_PYbucks):
    acessar_conta = input("Digite o nome da sua conta: ")
    if acessar_conta in nomes:
        index = nomes.index(acessar_conta)  
        senha = input("Digite a senha da sua conta: ")
        if senhas[index] == senha:  
            areyousure = input("Tem certeza? Você irá acabar com seu bebezinho tamagochi? Digite 1 para DELETAR e 0 para cancelar (ele lhe ama e depende de você para viver): ")
            areyousure = int(areyousure)
            if areyousure == 1:
                nomes.pop(index)
                senhas.pop(index)
                saldo_PYbucks.pop(index)
                print("Conta deletada com sucesso... seu monstro...")
                print("")
            elif areyousure == 0:
                print("Muito bem! Você escolheu o certo...")
                print("")
            else:
                print("Opção inválida! A conta não foi deletada.")
                print("")
        else:
            print("ERRO!! A senha está errada!")
            print("")
    else:
        print("ERRO!! O nome da conta não foi encontrado!") 
        print("")
#========================================================================================================================================================================================
#========================================================================================================================================================================================
def alterar_conta(nomes, senhas):
    acessar_conta = input("Digite o nome da sua conta: ") 
    if acessar_conta in nomes:
        acessarcontabool = 1
        index = nomes.index(acessar_conta)  
    else:
        print("Valor inválido!")
        print("")
        return  
    senha = input("Digite a senha da sua conta: ")
    if senhas[index] == senha:  
        senhabool = 1
    else:
        print("Valor inválido!")
        print("")
        return  
    novo_nome = input("Qual será o nome da sua conta? ")
    nova_senha = input("Qual será a senha da sua conta? ")

    nomes[index] = novo_nome
    senhas[index] = nova_senha
    print("Conta atualizada com sucesso!")
#========================================================================================================================================================================================
#========================================================================================================================================================================================
def observar_pet(nomes, pet_chapeu,chapeu):
    acessar_conta = input("Digite o nome da sua conta: ") 
    if acessar_conta in nomes:
        index = nomes.index(acessar_conta)
        chapeu = pet_chapeu[index]
        if chapeu == 1:
            chapeu_mexicano()
        elif chapeu == 2:
            chapeu_cartola()  
        elif chapeu == 3:
            orelhas_gato()
        elif chapeu == 4:
            chapeu_crianca()
        else:
            calvo()
        pet_feliz()
        print("")
    else:
        print("Valor inválido!")
        print("")
#========================================================================================================================================================================================
#========================================================================================================================================================================================
def alterar_pet(nomes, senhas, pet_chapeu):
    acessar_conta = input("Digite o nome da sua conta: ") 
    if acessar_conta in nomes:
        index = nomes.index(acessar_conta)  
    else:
        print("Valor inválido!")
        print("")
        return  
    senha = input("Digite a senha da sua conta: ")
    if senhas[index] == senha:  
        print("")
        print("Qual será o chapéu do seu Pet? (ele vem predefinido como Careca)")
        print("0 para chapéu mexicano ")
        print("1 para cartola ")
        print("2 para orelhas de gato ")
        print("3 para chapéu de criança ")
        chapeu = input("Qual chapéu deseja? ")
        chapeu = int(chapeu)
        if chapeu in [0,1,2,3]:
            pet_chapeu[index] == chapeu
            print("Chapéu atualizado com sucesso!")
            print("")
        else:
            print("Opção inválida! Por favor, escolha um número de 1 a 4.")
            print("")
    else:
        print("Senha inválida!")
        print("")
sistema_base(nomes, senhas)