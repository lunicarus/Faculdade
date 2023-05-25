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
def submenu_filmes():
    print("Submenu de Filmes:")
    print("1. Listar todos os filmes")
    print("2. Listar um filme específico")
    print("3. Incluir um filme")
    print("4. Alterar um filme")
    print("5. Excluir um filme")

# Função para exibir o submenu de sessões
def submenu_sessoes():
    print("Submenu de Sessões:")
    print("1. Listar todas as sessões")
    print("2. Listar uma sessão específica")
    print("3. Incluir uma sessão")
    print("4. Alterar uma sessão")
    print("5. Excluir uma sessão")

# Função para exibir o submenu de relatórios
def submenu_relatorios():
    print("Submenu de Relatórios:")
    print("1. Mostrar todas as salas com tipo de exibição X e capacidade maior que Y")
    print("2. Mostrar todos os filmes lançados a partir do ano X")
    print("3. Mostrar todas as sessões exibidas entre as datas X e Y")

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
    print("Código:", sala["codigo"])
    print("Nome:", sala["nome"])
    print("Capacidade:", sala["capacidade"])
    print("Tipo de Exibição:", sala["tipo_exibicao"])
    print("Acessível:", sala["acessivel"])

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
    salas = {}
    filmes = {}
    sessoes = {}

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            submenu_salas()
            # Implemente as operações do submenu de salas
            # Listar todas, Listar uma, Incluir, Alterar, Excluir

        elif opcao == "2":
            submenu_filmes()
            # Implemente as operações do submenu de filmes
            # Listar todos, Listar um, Incluir, Alterar, Excluir

        elif opcao == "3":
            submenu_sessoes()
            # Implemente as operações do submenu de sessões
            # Listar todas, Listar uma, Incluir, Alterar, Excluir

        elif opcao == "4":
            submenu_relatorios()
            relatorio_opcao = input("Escolha uma opção de relatório: ")

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
                print("Opção inválida. Tente novamente.")

        elif opcao == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()