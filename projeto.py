import re
from datetime import datetime

#region Filmes
def SubmenuFilmes(filmes,sessoes):

    escolhaMenuFilme = 0
    while escolhaMenuFilme != '6':
        print("Submenu de Filmes:")
        print("1. Listar todos os filmes")
        print("2. Listar um filme específico")
        print("3. Incluir um filme")
        print("4. Alterar um filme")
        print("5. Excluir um filme")
        print("6. Sair")
        print("\n")
        escolhaMenuFilme = input("Escolha uma opçao: ")
        if escolhaMenuFilme == '1':
            for filme in filmes:
                print("\n")
                print("-------------------------")
                print("Codigo: ",filme)
                ExibirDadosFilme(filmes[filme])
        elif escolhaMenuFilme == '2':
            ExibirDadosFilme(BuscarFilme(filmes))
            print("\n")
        elif escolhaMenuFilme == '3':
            IncluirFilme(filmes)
            print("\n")
        elif escolhaMenuFilme == '4':
            AlterarFilme(filmes,sessoes)
            print("\n")
        elif escolhaMenuFilme == '5':
            ExcluirFilme(filmes,sessoes)
            print("\n")
        elif escolhaMenuFilme == '6':
            print("saindo do menu filmes...")
        else:
            print("opção invalida!")
            print("\n")
        
def ExibirDadosFilme(filme):
        print("Nome:", filme["Nome"])
        print("Ano de Lançamento:", filme["Ano de Lançamento"])
        print("Diretor:", filme["Diretor"])
        print("Atores:", ", ".join(filme["Atores"]))
        print("-------------------------")

def BuscarFilme(filmes):
    codigo = int(input("Digite o código do filme: "))
    if codigo in filmes:
        print("-------------------------")
        print("Codigo: ",codigo)
        filme = filmes[codigo]
        return filme
    else:
        print("Filme não encontrado.")

def IncluirFilme(filmes):
    codigo = int(input("Digite o código do filme: "))
    if codigo in filmes:
        print("Filme já cadastrado.")
    else:
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

def AlterarFilme(filmes,sessoes):
    codigo = int(input("Digite o código do filme que deseja alterar: "))
    if codigo in filmes:
        for sessao in sessoes:
            if sessao[0] == codigo:
                print("não é possivel alterar filme pois o mesmo faz parte de uma sessão")
                return
            else:
                continue
        filme = filmes[codigo]
        ExibirDadosFilme(filme)

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

def ExcluirFilme(filmes,sessoes):
    codigo = int(input("Digite o código do filme que deseja excluir: "))
    if codigo in filmes:
        for sessao in sessoes:
            if sessao[0] == codigo:
                print("não é possivel excluir filme pois o mesmo faz parte de uma sessão")
                return
            else:
                continue
        del filmes[codigo]
        print("Filme excluído com sucesso.")
    else:
        print("Filme não encontrado.")
#endregion

# region Salas
def SubmenuSalas(salas,sessoes):
    escolhaMenuSala = '0'
    while escolhaMenuSala != '6':
        print("Submenu de Salas:")
        print("1. Listar todas as salas")
        print("2. Listar uma sala específico")
        print("3. Incluir uma sala")
        print("4. Alterar uma sala")
        print("5. Excluir uma sala")
        print("6. Sair")
        escolhaMenuSala = input("Escolha uma opção: ")
        print("\n")
        if escolhaMenuSala == '1':
            for sala in salas: 
                #'sala' é o codigo de uma sala, que está presente no dicionario salas
                print("\n")
                print("-------------------------")
                print("Codigo: ",sala)
                ExibirDadosSala(salas[sala]) #recebe os valores atrelados a Key
        elif escolhaMenuSala == '2':
            BuscaSalaExibe(salas)
            print("\n")
        elif escolhaMenuSala == '3':
            IncluirSala(salas)
            print("\n")
        elif escolhaMenuSala == '4':
            AlterarSala(salas,sessoes)
            print("\n")
        elif escolhaMenuSala == '5':
            ExcluirSala(salas,sessoes)
            print("\n")
        elif escolhaMenuSala == '6':
            print("saindo do submenu salas...")
        else :
            print("opção invalida!")
            print("\n")
        
def ExibirDadosSala(sala):
    print(f"Nome: {sala['Nome']}")
    print(f"Capacidade: {sala['Capacidade']}")
    print(f"Tipo de Exibição: {sala['Tipo de Exibição']}")
    print(f"Acessível: {sala['Acessível']}")
    print("-------------------------")

def BuscaSalaExibe(salas):
    codigo = int(input("Digite o código da sala: "))
    if codigo in salas:
        sala = salas[codigo]
        print("-------------------------")
        print("Codigo: ",codigo)
        ExibirDadosSala(sala)
    else:
        print("Sala não encontrada.")

def IncluirSala(salas):
    codigo = int(input("Digite o código da sala: "))
    if codigo in salas:
        print("Sala já cadastrada.")
    else:
        nome = input("Digite o nome da sala: ")

        Capacidade = int(input("Digite a capacidade: "))
        while Capacidade < 0 or Capacidade > 1000:
            print(" valor invalido! ")
            Capacidade = int(input("Digite a capacidade: "))

        TipoExibicao = input("Digite o tipo de Exibição (2D / 3D): ").upper()
        while TipoExibicao != "2D" and TipoExibicao != "3D":
            print(" valor invalido! ")
            TipoExibicao = input("Digite o tipo de Exibição (2D / 3D): ").upper()

        acessivel = input( "digite 'S' para acessivel e 'N' para nao acessivel: ").upper()
        while acessivel != 'S' and acessivel != 'N':
            print(" valor invalido! ")
            acessivel = input( "digite 'S' para acessivel e 'N' para nao acessivel: ").upper()
        if acessivel == 'S':
            acessivel = 'Sim'
        else:
            acessivel = 'Não'
        
        salas[codigo] = {
            "Nome": nome,
            "Capacidade": Capacidade,
            "Tipo de Exibição": TipoExibicao,
            "Acessível": acessivel
        }
        print("sala cadastrada com sucesso.")

def AlterarSala(salas,sessoes):
    codigo = int(input("Digite o código da sala que deseja alterar: "))
    if codigo in salas:
            for sessao in sessoes:
                if sessao[1] == codigo:
                    print("não é possivel alterar sala pois a mesma faz parte de uma sessão")
                    return
                else:
                    continue
    if codigo in salas:
        sala = salas[codigo]
        ExibirDadosSala(sala)

        nome = input("Digite o novo nome da sala (ou deixe em branco para manter o mesmo): ")
        if nome:
            sala["Nome"] = nome

        capacidade = input("Digite a nova capacidade (ou deixe em branco para manter o mesmo): ")
        if capacidade:
            capacidade = int(capacidade)
            if capacidade > 0 and capacidade < 1000:
                sala["Capacidade"] = capacidade 
        
        TipoExibição = input("Digite o novo tipo de exibição (2D/3D) (ou deixe em branco para manter o mesmo): ").upper()
        if TipoExibição:
            if TipoExibição == '2D' or TipoExibição ==  '3D':
                sala["Tipo de Exibição"] = TipoExibição

        acessivel = input("Digite o novo estado de acessibilidade (ou deixe em branco para manter o mesmo): ").upper()
        if acessivel:
            if acessivel == 'S':
                acessivel = 'Sim'
                sala["Capacidade"] = acessivel
            elif acessivel == 'N':
                acessivel = 'Não'
                sala["Capacidade"] = acessivel

        print("sala alterada com sucesso.")
    else:
        print("sala não encontrada.")

def ExcluirSala(salas,sessoes):
    codigo = int(input("Digite o código da sala que deseja excluir: "))
    if codigo in salas:
            for sessao in sessoes:
                if sessao[1] == codigo:
                    print("não é possivel excluir sala pois a mesma faz parte de uma sessão")
                    return
                else:
                    continue
            del salas[codigo]
            print("sala excluída com sucesso.")
    else:
        print("sala não encontrada.")

#endregion

#region Sessões


def SubmenuSessoes(sessoes,filmes,salas):
    escolhaMenuSessao = '0'
    while escolhaMenuSessao != '6':
        print("Submenu de sessoes:")
        print("1. Listar todas as sessoes")
        print("2. Listar uma sessão específico")
        print("3. Incluir uma sessão")
        print("4. Alterar uma sessão")
        print("5. Excluir uma sessão")
        print("6. Sair")
        escolhaMenuSessao = input("Escolha uma opção: ")
        print("\n")
        if escolhaMenuSessao == '1':
            for sessao in sessoes:
                print("\n")
                print("-------------------------")
                ExibirDadosNaKey(sessao, filmes) 
                precoIngresso(sessoes[sessao])
                #exibir dados sessão mostra os dados que fazem parte da key
                #exibir dados sessão key mostra os dados atrelados a key
        elif escolhaMenuSessao == '2':
            BuscaSessaoExibe(sessoes,filmes,salas)
            print("\n")
        elif escolhaMenuSessao == '3':
            IncluirSessao(filmes,salas,sessoes)
            print("\n")
        elif escolhaMenuSessao == '4':
            AlterarSessao(filmes,salas,sessoes)
            print("\n")
        elif escolhaMenuSessao == '5':
            ExcluirSessao(filmes,salas,sessoes)
            print("\n")
        elif escolhaMenuSessao == '6':
            print("saindo do submenu sessoes...")
        else :
            print("opção invalida!")
            print("\n") 

def precoIngresso(sessaoKey):
    print(f"Preço do Ingresso: R${sessaoKey['Preço do Ingresso']}")
def ExibirDadosNaKey(sessao, filmes):
    cod=sessao[0]
    valores=filmes[cod]
    nome=valores['Nome']
    print('Nome: ',nome)
    print(f"Código do Filme: {sessao[0]}")
    print(f"Código da Sala: {sessao[1]}")
    print(f"Data: {sessao[2]}")
    print(f"Horário: {sessao[3]}")
#region CRUD   
def IncluirSessao(filmes,salas,sessoes):
    codSala = int(input("Digite o código da sala: "))
    while codSala not in salas:
        print("codigo de sala inexistente, digite novamente")
        codSala = int(input("Digite o código da sala: "))
    codFilme = int(input("Digite o codigo do filme: "))
    while codFilme not in filmes:
        print("codigo de filme inexistente, digite novamente")
        codFilme = int(input("Digite o código do filme: "))
 
    def HoraData():
        Horario = ''
        while not Horario:
            horarioS = input("digite o horario no formato HH:MM: ")
            testeH = (horarioS.split(":"))
            for elemento in range(len(testeH)):
                testeH[elemento] = int(testeH[elemento])
            if testeH[0] < 0 or testeH[0] > 24 or testeH[1] < 0 or testeH[1] > 60:
                print("valor para horas ou minutos invalido!")
                continue
            r = re.compile('.{2}:.{2}')
            if len(horarioS) == 5:
                if r.match(horarioS):
                    Horario = horarioS
                else:
                    print("formatação invalida, digite novamente")
        Data = ''
        while not Data:       
            DataS= input("Digite a data no formato DD/MM/AAAA: ")
            testeD = (DataS.split("/"))
            for elemento in range(len(testeD)):
                testeD[elemento] = int(testeD[elemento])
            if testeD[0] < 0 or testeD[0] > 31 or testeD[1] < 0 or testeD[1] > 12 or testeD[2] < 2023 or testeD[2] > 2027:
                print("data invalida!")
                continue;
            r = re.compile('.{2}/.{2}/.{4}')
            if len(DataS) == 10:
                if r.match(DataS):
                    Data = DataS
                else:
                    print("formatação invalida, digite novamente")

        return (Data,Horario)
    data = ''
    horario = ''
    data,horario = HoraData()
    while (codFilme,codSala,data,horario) in sessoes:
        print("data e horario ja ocupados para esta sala! escolha outro horario")
        data,horario = HoraData()
    precoingresso = -1
    while precoingresso < 0 or precoingresso > 200:
        precoingresso = float(input("digite um valor para o ingresso: "))
    sessoes[(codFilme,codSala,data,horario)] = {
            "Preço do Ingresso": precoingresso
        }

def ExcluirSessao(filmes,salas,sessoes):
    CodExcluir = BuscaSessaoRetornaKey(filmes,salas)
    if CodExcluir in sessoes:
        del sessoes[CodExcluir]
        print("sessão excluida com sucesso")
    else:
        print("não foi possivel excluir")

def AlterarSessao(filmes,salas,sessoes):
    codAlterar = BuscaSessaoRetornaKey(filmes,salas)
    if codAlterar in sessoes:
        sessao = sessoes[codAlterar]
        ExibirDadosNaKey(codAlterar, filmes)
        precoIngresso(sessao)
        preco = input("Digite o novo preço da sessão (ou deixe em branco para manter o mesmo): ")
        if preco:
            sessao["Preço do Ingresso"] = float(preco)
        print("sessão alterada com sucesso.")
    else:
        print("Filme não encontrado.")


#endregion

#region BuscasSessoes
def BuscaSessaoRetornaKey(filmes,salas):
    codSala = int(input("Digite o código da sala: "))
    while codSala not in salas:
        print("codigo de sala inexistente, digite novamente")
        codSala = int(input("Digite o código da sala: "))
    codSalaSimples = codSala
    codSala = salas[codSala]
    codFilme = int(input("Digite o codigo do filme: "))
    while codFilme not in filmes:
        print("codigo de filme inexistente, digite novamente")
        codFilme = int(input("Digite o código do filme: "))
    codFilmeSimples = codFilme
    codFilme = filmes[codFilme]
    
    Horario = ''
    while not Horario:
        horarioS = input("digite o horario no formato HH:MM: ")
        testeH = (horarioS.split(":"))
        for elemento in range(len(testeH)):
            testeH[elemento] = int(testeH[elemento])
        if testeH[0] < 0 or testeH[0] > 24 or testeH[1] < 0 or testeH[1] > 60:
            print("valor para horas ou minutos invalido!")
            continue
        r = re.compile('.{2}:.{2}')
        if len(horarioS) == 5:
            if r.match(horarioS):
                Horario = horarioS
            else:
                print("formatação invalida, digite novamente")
        else:
            print("numero de caracteres invalido, digite novamente")
    Data = ''
    while not Data:       
        DataS= input("Digite a data no formato DD/MM/AAAA: ")
        testeD = (DataS.split("/"))
        for elemento in range(len(testeD)):
            testeD[elemento] = int(testeD[elemento])
        if testeD[0] < 0 or testeD[0] > 31 or testeD[1] < 0 or testeD[1] > 12 or testeD[2] < 2023 or testeD[2] > 2027:
            print("data invalida!")
            continue;
        r = re.compile('.{2}/.{2}/.{4}')
        if len(DataS) == 10:
            if r.match(DataS):
                Data = DataS
            else:
                print("formatação invalida, digite novamente")
        else:
            print("numero de caracteres invalido, digite novamente")
    return (codFilmeSimples,codSalaSimples,Data,Horario)
def BuscaSessaoExibe(sessoes,filmes,salas):    

    codSessao = BuscaSessaoRetornaKey(filmes,salas)
    if codSessao in sessoes:
        print("-------------------------")
        ExibirDadosNaKey(codSessao, filmes)
        precoIngresso(sessoes[codSessao])
    else:
        print("Sala não encontrada.")
#endregion

#endregion

#region Relatorios
def relatorioOpcoes(relatorio_opcao,salas,filmes,sessoes):
        
    if relatorio_opcao == 1:
            tipo_exibicao = input("Digite o tipo de exibição (3D/2D): ").upper()
            capacidade = int(input("Digite a capacidade mínima (1~200): "))
            RelatoriosSalasTipoCapacidade(salas, tipo_exibicao, capacidade)
    elif relatorio_opcao == 2:
            ano = int(input("Digite o ano mínimo: "))
            RelatorioFilmesLancados(filmes, ano)

    elif relatorio_opcao == 3:
            data_inicial = input("Digite a data inicial (formato: DD/MM/AAAA): ")
            data_final = input("Digite a data final (formato: DD/MM/AAAA): ")
            RelatorioSessoesData(sessoes, filmes,data_inicial, data_final)

    else:
        print("Opção inválida.")

def SubmenuRelatorios(salas,filmes,sessoes):
    relatorio_opcao = 0
    while relatorio_opcao != 4:

        print("Submenu de Relatórios:")
        print("1. Mostrar todas as salas com tipo de exibição X e capacidade maior que Y")
        print("2. Mostrar todos os filmes lançados a partir do ano X")
        print("3. Mostrar todas as sessões exibidas entre as datas X e Y")
        print("4. Sair")
        relatorio_opcao = int(input("Escolha: "))
        relatorioOpcoes(relatorio_opcao,salas,filmes,sessoes)

def RelatoriosSalasTipoCapacidade(salas, tipo_exibicao, capacidade):
    salas_encontradas = []
    for sala in salas.values(): 
        #.values() faz com que o for acesse somente os valores em salas, como uma lista
        #no caso, não há o acesso das keys
        if sala["Tipo de Exibição"] == tipo_exibicao and sala["Capacidade"] > capacidade:
            salas_encontradas.append(sala)
    if len(salas_encontradas) == 0:
        print("Nenhuma sala encontrada com os critérios especificados.")
    else:
        print("Salas encontradas:")
        for sala in salas_encontradas:
            ExibirDadosSala(sala)
            print("")

def RelatorioFilmesLancados(filmes, ano):
    filmes_encontrados = []
    for filme in filmes.values():
        if filme["Ano de Lançamento"] >= ano:
            filmes_encontrados.append(filme)
    if len(filmes_encontrados) == 0:
        print("Nenhum filme encontrado com os critérios especificados.")
    else:
        print("Filmes encontrados:")
        for filme in filmes_encontrados:
            ExibirDadosFilme(filme)
            print("")

def RelatorioSessoesData(sessoes,filmes,dataInicio,DataFim):
    try:
        DataI  = datetime.strptime(dataInicio, "%d/%m/%Y")
        DataF= datetime.strptime(DataFim, "%d/%m/%Y")      
    except ValueError:
        print("Datas inválidas.")
        return
    sessoes_encontradas = []
    for sessao, sessao_key in sessoes.items():
        DataE = datetime.strptime( sessao[2], "%d/%m/%Y")
        if DataI <= DataE <= DataF:
            sessoes_encontradas.append((sessao, sessao_key))
    if len(sessoes_encontradas) > 0:
        print(f"Sessões encontradas entre {dataInicio} e {DataFim}")
        for sessao, sessao_key in sessoes_encontradas:
            print("-------------------------")
            ExibirDadosNaKey(sessao, filmes)
            precoIngresso(sessao_key)
    else:
        print(f"Não foram encontradas sessões entre {dataInicio} e {DataFim}")

#endregion

#region Main
def ExibirMenu():
    print("Menu de Opções:")
    print("1. Submenu de Salas")
    print("2. Submenu de Filmes")
    print("3. Submenu de Sessões")
    print("4. Submenu Relatórios")
    print("5. Sair")

def main():
    salas = {}
    filmes = {}
    sessoes = {}
    (salas,filmes,sessoes) = AdicionarDadosExemplo()
    ExibirMenu()
    opcao="0"
    while opcao != '5':
        
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            SubmenuSalas(salas,sessoes)
        elif opcao == "2":
            SubmenuFilmes(filmes,sessoes)
        elif opcao == "3":
            SubmenuSessoes(sessoes,filmes,salas)
        elif opcao == "4":
            print("em progresso")
            SubmenuRelatorios(salas,filmes,sessoes)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def AdicionarDadosExemplo():
    salas = {
        101: {"Nome": "Sala Sul", "Capacidade": 100, "Tipo de Exibição": "2D", "Acessível": 'Sim'},
        102: {"Nome": "Sala Norte", "Capacidade": 80, "Tipo de Exibição": "3D", "Acessível": 'Não'},
        201: {"Nome": "Sala Leste", "Capacidade": 120, "Tipo de Exibição": "2D", "Acessível": 'Sim'},
        202: {"Nome": "Sala Oeste", "Capacidade": 90, "Tipo de Exibição": "3D", "Acessível": 'Sim'},
        301: {"Nome": "Sala A", "Capacidade": 150, "Tipo de Exibição": "2D", "Acessível": 'Não'},
        302: {"Nome": "Sala B", "Capacidade": 100, "Tipo de Exibição": "3D", "Acessível": 'Sim'},
        401: {"Nome": "Sala C", "Capacidade": 100, "Tipo de Exibição": "2D", "Acessível": 'Sim'},
        402: {"Nome": "Sala D", "Capacidade": 80, "Tipo de Exibição": "3D", "Acessível":'Não'},
        501: {"Nome": "Sala VIP", "Capacidade": 120, "Tipo de Exibição": "2D", "Acessível": 'Sim'},
        502: {"Nome": "Sala VVIP", "Capacidade": 90, "Tipo de Exibição": "3D", "Acessível": 'Sim'}
    }

    filmes = {
        1: {"Nome": "Tentando Ensinar: A Saga", "Ano de Lançamento": 2023, "Diretor": "__", "Atores": ["C", "Python","Aluno"]},
        2: {"Nome": "The Infinite Loop", "Ano de Lançamento": 2001, "Diretor": "ari aster", "Atores": ["maicao", "estagiario 015A"]},
        3: {"Nome": "Deadpool 7: Idoso antiheroi Imortal", "Ano de Lançamento": 2023, "Diretor": "Michael Bay", "Atores": ["maicao", "Carlos"]},
        4: {"Nome": "Vingadores 10: Mais uma ameaça chata", "Ano de Lançamento": 2023, "Diretor": "Michael Bay", "Atores": ["Fernando", "arthur"]},
        5: {"Nome": "Algoritmo: A Definição", "Ano de Lançamento": 2022, "Diretor": "Michael Bay", "Atores": ["Paulo", "catarina"]},
        6: {"Nome": "Carlos", "Ano de Lançamento": 1999, "Diretor": "Michael Bay", "Atores": ["Paulo", "catarina"]},
        7: {"Nome": "Carlos II: O matador", "Ano de Lançamento": 2011, "Diretor": "Michael Bay", "Atores": ["Paulo", "catarina"]},
        8: {"Nome": "Carlos III: A vingança", "Ano de Lançamento": 1016, "Diretor": "Michael Bay", "Atores": ["Paulo", "catarina"]},
        9: {"Nome": "Carlos IV: O sucessor", "Ano de Lançamento": 2019, "Diretor": "Michael Bay", "Atores": ["Paulo", "catarina"]},
        10: {"Nome": "Carlos V: Ciborgues Mortais", "Ano de Lançamento": 2023, "Diretor": "Michael Bay", "Atores": ["Paulo", "catarina"]}
    }

    sessoes = {
        (1, 101, "11/06/2023", "10:00"): {"Preço do Ingresso": 15.0},
        (2, 102, "20/06/2023", "13:00"): {"Preço do Ingresso": 20.0},
        (3, 201, "30/06/2023", "16:00"): {"Preço do Ingresso": 18.0},
        (4, 202, "12/06/2023", "10:00"): {"Preço do Ingresso": 16.0},
        (5, 301, "22/06/2023", "13:00"): {"Preço do Ingresso": 22.0},
        (6, 302, "02/06/2023", "16:00"): {"Preço do Ingresso": 17.0},
        (7, 401, "09/06/2023", "10:00"): {"Preço do Ingresso": 15.0},
        (8, 402, "06/06/2023", "13:00"): {"Preço do Ingresso": 20.0},
        (9, 501, "15/06/2023", "16:00"): {"Preço do Ingresso": 18.0},
        (10,502, "01/06/2023", "10:00"): {"Preço do Ingresso": 16.0}
    }

    return salas, filmes, sessoes
main()
#endregion