# Função para exibir o menu principal
def exibir_menu():
    print("Menu de Opções:")
    print("1. Submenu de Salas")
    print("2. Submenu de Filmes")
    print("3. Submenu de Sessões")
    print("4. Submenu Relatórios")
    print("5. Sair")

# Função para exibir o submenu de salas
def submenu_salas():
    print("Submenu de Salas:")
    print("1. Listar todas as salas")
    print("2. Listar uma sala específica")
    print("3. Incluir uma sala")
    print("4. Alterar uma sala")
    print("5. Excluir uma sala")


# Função para exibir o submenu de filmes
def submenu_filmes(filmes):

    print("Submenu de Filmes:")
    print("1. Listar todos os filmes")
    print("2. Listar um filme específico")
    print("3. Incluir um filme")
    print("4. Alterar um filme")
    print("5. Excluir um filme")
    print("6. Sair")
    escolhaMenuFilme = input("Escolha: ")
    while escolhaMenuFilme != '6':
        if escolhaMenuFilme == '1':
            for filme in filmes:
                exibir_dados_filme(filme)
        elif escolhaMenuFilme == '2':
                buscar_filme(filmes)
        elif escolhaMenuFilme == '3':
                incluir_filme(filmes)
        elif escolhaMenuFilme == '4':
            alterar_filme(filmes)
        elif escolhaMenuFilme == '5':
            excluir_filme(filmes)
        else:
            print("opção invalida!")
        
    

def listar_filmes(filmes):
    print("=== Lista de Filmes ===")
    for codigo, filme in filmes.items():
        print("Código:", codigo)
        print("Nome:", filme["Nome"])
        print("Ano de Lançamento:", filme["Ano de Lançamento"])
        print("Diretor:", filme["Diretor"])
        print("Atores:", ", ".join(filme["Atores"]))
        print("-----------------------")

def buscar_filme(filmes):
    codigo = input("Digite o código do filme: ")
    if codigo in filmes:
        filme = filmes[codigo]
        print("=== Detalhes do Filme ===")
        print("Código:", codigo)
        print("Nome:", filme["Nome"])
        print("Ano de Lançamento:", filme["Ano de Lançamento"])
        print("Diretor:", filme["Diretor"])
        print("Atores:", ", ".join(filme["Atores"]))
        print("-------------------------")
    else:
        print("Filme não encontrado.")

def incluir_filme(filmes):
    codigo = input("Digite o código do filme: ")
    if codigo in filmes:
        print("Filme já cadastrado.")
        return

    nome = input("Digite o nome do filme: ")
    ano = int(input("Digite o ano de lançamento do filme: "))
    diretor = input("Digite o nome do diretor do filme: ")
    atores = input("Digite os nomes dos atores do filme (separados por vírgula): ").split(",")

    filmes[codigo] = {
        "Nome": nome,
        "Ano de Lançamento": ano,
        "Diretor": diretor,
        "Atores": atores
    }

    print("Filme cadastrado com sucesso.")

def alterar_filme(filmes):
    codigo = input("Digite o código do filme que deseja alterar: ")
    if codigo in filmes:
        filme = filmes[codigo]
        print("=== Detalhes do Filme ===")
        print("Código:", codigo)
        print("Nome:", filme["Nome"])
        print("Ano de Lançamento:", filme["Ano de Lançamento"])
        print("Diretor:", filme["Diretor"])
        print("Atores:", ", ".join(filme["Atores"]))
        print("-------------------------")

        nome = input("Digite o novo nome do filme (ou deixe em branco para manter o mesmo): ")
        if nome:
            filme["Nome"] = nome

        ano = input("Digite o novo ano de lançamento do filme (ou deixe em branco para manter o mesmo): ")
        if ano:
            filme["Ano de Lançamento"] = int(ano)

        diretor = input("Digite o novo diretor do filme (ou deixe em branco para manter o mesmo): ")
        if diretor:
            filme["Diretor"] = diretor

        atores = input("Digite os novos atores do filme (separados por vírgula) "
                       "(ou deixe em branco para manter os mesmos): ").split(",")
        if atores:
            filme["Atores"] = atores

        print("Filme alterado com sucesso.")
    else:
        print("Filme não encontrado.")

def excluir_filme(filmes):
    codigo = input("Digite o código do filme que deseja excluir: ")
    if codigo in filmes:
        del filmes[codigo]
        print("Filme excluído com sucesso.")
    else:
        print("Filme não encontrado.")

# Função para exibir o submenu de sessões
def submenu_sessoes():
    print("Submenu de Sessões:")
    print("1. Listar todas as sessões")
    print("2. Listar uma sessão específica")
    print("3. Incluir uma sessão")
    print("4. Alterar uma sessão")
    print("5. Excluir uma sessão")
def relatorioOpcoes(relatorio_opcao,salas,filmes,sessoes):
        
    if relatorio_opcao == "1":
            tipo_exibicao = input("Digite o tipo de exibição (X): ")
            capacidade = int(input("Digite a capacidade mínima (Y): "))
            relatorio_salas_tipo_capacidade(salas, tipo_exibicao, capacidade)
    elif relatorio_opcao == "2":
            ano = int(input("Digite o ano mínimo (X): "))
            relatorio_filmes_lancados(filmes, ano)

    elif relatorio_opcao == "3":
            data_inicial = input("Digite a data inicial (formato: DD/MM/AAAA): ")
            data_final = input("Digite a data final (formato: DD/MM/AAAA): ")
            relatorio_sessoes_data(sessoes, data_inicial, data_final)

    else:
        print("Opção inválida.")
# Função para exibir o submenu de relatórios
def submenu_relatorios(salas,filmes,sessoes):
    print("Submenu de Relatórios:")
    print("1. Mostrar todas as salas com tipo de exibição X e capacidade maior que Y")
    print("2. Mostrar todos os filmes lançados a partir do ano X")
    print("3. Mostrar todas as sessões exibidas entre as datas X e Y")
    relatorio_opcao = input("Escolha: ")
    relatorioOpcoes(relatorio_opcao,salas,filmes,sessoes)

# Função para listar todas as salas com tipo de exibição X e capacidade maior que Y
def relatorio_salas_tipo_capacidade(salas, tipo_exibicao, capacidade):
    salas_encontradas = []
    for sala in salas.values():
        if sala["tipo_exibicao"] == tipo_exibicao and sala["capacidade"] > capacidade:
            salas_encontradas.append(sala)
    if len(salas_encontradas) == 0:
        print("Nenhuma sala encontrada com os critérios especificados.")
    else:
        print("Salas encontradas:")
        for sala in salas_encontradas:
            exibir_dados_sala(sala)
            print("")

# Função para listar todos os filmes lançados a partir do ano X
def relatorio_filmes_lancados(filmes, ano):
    filmes_encontrados = []
    for filme in filmes.values():
        if filme["ano_lancamento"] >= ano:
            filmes_encontrados.append(filme)
    if len(filmes_encontrados) == 0:
        print("Nenhum filme encontrado com os critérios especificados.")
    else:
        print("Filmes encontrados:")
        for filme in filmes_encontrados:
            exibir_dados_filme(filme)
            print("")

# Função para listar todas as sessões exibidas entre as datas X e Y
def relatorio_sessoes_data(sessoes, data_inicial, data_final):
    sessoes_encontradas = []
    for sessao in sessoes.values():
        if data_inicial <= sessao["data"] <= data_final:
            sessoes_encontradas.append(sessao)
    if len(sessoes_encontradas) == 0:
        print("Nenhuma sessão encontrada com os critérios especificados.")
    else:
        print("Sessões encontradas:")
        for sessao in sessoes_encontradas:
            exibir_dados_sessao(sessao)
            print("")

# Função para exibir os dados de uma sala
def exibir_dados_sala(sala):
    print("Código:", sala[0])
    print("Nome:", sala[1])
    print("Capacidade:", sala[2])
    print("Tipo de Exibição:", sala[3])
    print("Acessível:", sala[4])

def verifica(cod, salas):
    for sala in salas:
        if cod==sala[0]:
            print()
            print('* Não é possível adicionar uma sala com este código, tente novamente! *')
            print()
            return False

def verifica2(mud, salas):
    ver=False
    for sala in salas:
        if mud==sala[0]:
            print()
            print('Sala encontrada!')
            print()
            
            altera(sala)
            print()
            ver=True
            return False          
    if ver!=True:
        print("Sala não encontrada, tente novamente")
    

def altera(sala):
    print(f'Sala escolhida: {sala[1]}')
    print("O que de seja mudar?")
    print(" 1. Nome: ", sala[1])
    print(" 2. Capacidade: ", sala[2])
    print(" 3. Tipo de exibição: ", sala[3])
    print(" 4. Acessível: ", sala[4])
    print(" 5. Cancelar")
    
    op=int(input("Escolha uma opção: "))        
    if op == 1:
        nv_nome=input("Insira o novo nome da sala: ")
        sala[1]=nv_nome
        print()
        print("Nome da sala alterado com sucesso!")
    elif op==2:
        nv_capacidade=int(input("Insira a nova capacidade: "))
        sala[2]=nv_capacidade
        print()
        print("Capacidade da sala alterado com sucesso!")
    elif op==3:
        nv_exibicao=input("Insira a nova capacidade: ")
        sala[3]=nv_exibicao
        print()
        print("Tipo de exibição da sala alterado com sucesso!")
    elif op==4:
        nv_acess=input("Insira a nova acessibilidade (Sim/Não): ")
        sala[4]=nv_acess
        print()
        print("Acessibilidade da sala alterada com sucesso!")
    elif op==5:
        print()
        print("Operação cancelada!")
    else:
        print("Opção inválida, tente novamente..")

def add_sala(salas):
    print('Insira as seguintes informações: ')
    nova_sala=[]
    cod=int(input("Código da sala: "))
    veri=verifica(cod, salas)
    if veri==False:
        return False
    else:
        nova_sala.append(cod)
        nome=input("Nome: ")
        nova_sala.append(nome)
        capacidade=int(input("Capacidade: "))
        nova_sala.append(capacidade)
        tipo_exi=input("Tipo de exibição: ")
        nova_sala.append(tipo_exi)
        acess=input("Acessibilidade (Sim/Não): ")
        nova_sala.append(acess)
        salas.append(nova_sala)
        print('Sala adicionada com sucesso!')
        print() 



# Função para exibir os dados de um filme
def exibir_dados_filme(filme):
    print("Código:", filme["codigo"])
    print("Nome:", filme["nome"])
    print("Ano de Lançamento:", filme["ano_lancamento"])
    print("Diretor:", filme["diretor"])
    print("Atores:", ", ".join(filme["atores"]))

# Função para exibir os dados de uma sessão
def exibir_dados_sessao(sessao):
    print("Código do Filme:", sessao["codigo_filme"])
    print("Código da Sala:", sessao["codigo_sala"])
    print("Data:", sessao["data"])
    print("Horário:", sessao["horario"])
    print("Preço do Ingresso:", sessao["preco_ingresso"])

# Função principal do programa
def main():
    salas = [[1, 'Sala A', 45, '3D', 'Sim'], [2, 'Sala B', 42, '2D', 'Não']]#cod, nome, capacidade, tipo de exibição, acessivel
    filmes = {}
    sessoes = {}

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        print()

        if opcao == "1":
            submenu_salas()
            # Implemente as operações do submenu de salas
            # Listar todas, Listar uma, Incluir, Alterar, Excluir
            op=input("Escolha uma opção: ")
            print()
            if op=="1": 
                for sala in salas:
                    print()
                    print(f"{sala[1]}:")
                    exibir_dados_sala(sala)
                    print()
                    
            elif op=='2':
                #o programa irá listar conforme a sala escolhida
                print('listar uma específica')
            
            elif op=='3':
                add_sala(salas)              
            
            elif op=='4':
                #pergunta qual sala deseja mudar
                print("Qual sala deseja alterar? ")
                mud=int(input(" Insira o código da sala: "))
                verifica2(mud, salas)           

        elif opcao == "2":
            submenu_filmes(filmes)
            # Implemente as operações do submenu de filmes
            # Listar todos, Listar um, Incluir, Alterar, Excluir

        elif opcao == "3":
            submenu_sessoes(sessoes)
            # Implemente as operações do submenu de sessões
            # Listar todas, Listar uma, Incluir, Alterar, Excluir

        elif opcao == "4":
            submenu_relatorios(salas,filmes,sessoes)

        elif opcao == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


def adicionar_dados_exemplo():
    salas = {
        "101": {"Nome": "Sala Sul", "Capacidade": 100, "Tipo de Exibição": "2D", "Acessível": True},
        "102": {"Nome": "Sala Norte", "Capacidade": 80, "Tipo de Exibição": "3D", "Acessível": False},
        "201": {"Nome": "Sala Leste", "Capacidade": 120, "Tipo de Exibição": "2D", "Acessível": True},
        "202": {"Nome": "Sala Oeste", "Capacidade": 90, "Tipo de Exibição": "3D", "Acessível": True},
        "301": {"Nome": "Sala A", "Capacidade": 150, "Tipo de Exibição": "2D", "Acessível": False},
        "302": {"Nome": "Sala B", "Capacidade": 100, "Tipo de Exibição": "3D", "Acessível": True},
        "401": {"Nome": "Sala C", "Capacidade": 100, "Tipo de Exibição": "2D", "Acessível": True},
        "402": {"Nome": "Sala D", "Capacidade": 80, "Tipo de Exibição": "3D", "Acessível": False},
        "501": {"Nome": "Sala VIP", "Capacidade": 120, "Tipo de Exibição": "2D", "Acessível": True},
        "502": {"Nome": "Sala VVIP", "Capacidade": 90, "Tipo de Exibição": "3D", "Acessível": True}
    }

    filmes = {
        "001": {"Nome": "Tentando Ensinar: A Saga", "Ano de Lançamento": 2023, "Diretor": "__", "Atores": ["C", "Python","Aluno"]},
        "002": {"Nome": "The Infinite Loop", "Ano de Lançamento": 2001, "Diretor": "ari aster", "Atores": ["maicao", "estagiario 015A"]},
        "003": {"Nome": "Deadpool 7: Idoso antiheroi Imortal", "Ano de Lançamento": 2023, "Diretor": "Michael Bay", "Atores": ["maicao", "Carlos"]},
        "004": {"Nome": "Vingadores 10: Mais uma ameaça chata", "Ano de Lançamento": 2023, "Diretor": "Michael Bay", "Atores": ["Fernando", "arthur"]},
        "005": {"Nome": "Algoritmo: A Definição", "Ano de Lançamento": 2022, "Diretor": "Michael Bay", "Atores": ["Paulo", "catarina"]},
        "006": {"Nome": "Carlos", "Ano de Lançamento": 1999, "Diretor": "Michael Bay", "Atores": ["Paulo", "catarina"]},
        "007": {"Nome": "Carlos II: O matador", "Ano de Lançamento": 2011, "Diretor": "Michael Bay", "Atores": ["Paulo", "catarina"]},
        "008": {"Nome": "Carlos III: A vingança", "Ano de Lançamento": 1016, "Diretor": "Michael Bay", "Atores": ["Paulo", "catarina"]},
        "009": {"Nome": "Carlos IV: O sucessor", "Ano de Lançamento": 2019, "Diretor": "Michael Bay", "Atores": ["Paulo", "catarina"]},
        "010": {"Nome": "Carlos V: Ciborgues Mortais", "Ano de Lançamento": 2023, "Diretor": "Michael Bay", "Atores": ["Paulo", "catarina"]}
    }

    sessoes = {
        ("001", "101", "11/06/2023", "10:00"): {"Preço do Ingresso": 15.0},
        ("002", "102", "21/06/2023", "13:00"): {"Preço do Ingresso": 20.0},
        ("003", "201", "31/06/2023", "16:00"): {"Preço do Ingresso": 18.0},
        ("004", "202", "12/06/2023", "10:00"): {"Preço do Ingresso": 16.0},
        ("005", "301", "22/06/2023", "13:00"): {"Preço do Ingresso": 22.0},
        ("006", "302", "02/06/2023", "16:00"): {"Preço do Ingresso": 17.0},
        ("007", "401", "09/06/2023", "10:00"): {"Preço do Ingresso": 15.0},
        ("008", "402", "06/06/2023", "13:00"): {"Preço do Ingresso": 20.0},
        ("009", "501", "15/06/2023", "16:00"): {"Preço do Ingresso": 18.0},
        ("010", "502", "01/06/2023", "10:00"): {"Preço do Ingresso": 16.0}
    }

    return salas, filmes, sessoes

if __name__ == "__main__":
    main()