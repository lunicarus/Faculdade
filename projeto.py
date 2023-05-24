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
    print("a) Mostrar todos os dados de todas as salas cujo tipo de exibição seja X e capacidade para mais de Y pessoas")
    print("b) Mostrar todos os dados de todos os filmes que foram lançados a partir do ano X")
    print("c) Mostrar os dados das sessões exibidas a partir de uma data inicial X até uma data final Y")

# Função para exibir relatório de salas
def relatorio_salas(salas, tipo_exibicao, capacidade_minima):
    print("Relatório de Salas:")
    for sala in salas:
        if sala['Tipo de exibição'] == tipo_exibicao and sala['Capacidade'] > capacidade_minima:
            print(f"Código: {sala['Código']}")
            print(f"Nome: {sala['Nome']}")
            print(f"Capacidade: {sala['Capacidade']}")
            print(f"Tipo de exibição: {sala['Tipo de exibição']}")
            print(f"Acessível: {sala['Acessível']}")
            print()

# Função para exibir relatório de filmes
def relatorio_filmes(filmes, ano_lancamento):
    print("Relatório de Filmes:")
    for filme in filmes:
        if filme['Ano de lançamento'] >= ano_lancamento:
            print(f"Código: {filme['Código']}")
            print(f"Nome: {filme['Nome']}")
            print(f"Ano de lançamento: {filme['Ano de lançamento']}")
            print(f"Diretor: {filme['Diretor']}")
            print(f"Atores: {', '.join(filme['Atores'])}")

# Função para exibir relatório de sessões
def relatorio_sessoes(sessoes, data_inicial, data_final):
    print("Relatório de Sessões:")
    for sessao in sessoes:
        if data_inicial <= sessao['Data'] <= data_final:
            print(f"Código do Filme: {sessao['Código do Filme']}")
            print(f"Código da Sala: {sessao['Código da Sala']}")
            print(f"Data: {sessao['Data']}")
            print(f"Horário: {sessao['Horário']}")
            print(f"Preço do Ingresso: {sessao['Preço do Ingresso']}")
            print()

# Função principal
def main():
    salas = []
    filmes = []
    sessoes = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":  # Submenu de Salas
            submenu_salas()
            opcao_salas = input("Escolha uma opção: ")

            if opcao_salas == "1":  # Listar todas as salas
                print("Listar todas as salas")

            elif opcao_salas == "2":  # Listar uma sala específica
                print("Listar uma sala específica")

            elif opcao_salas == "3":  # Incluir uma sala
                print("Incluir uma sala")

            elif opcao_salas == "4":  # Alterar uma sala
                print("Alterar uma sala")

            elif opcao_salas == "5":  # Excluir uma sala
                print("Excluir uma sala")

        elif opcao == "2":  # Submenu de Filmes
            submenu_filmes()
            opcao_filmes = input("Escolha uma opção: ")

            if opcao_filmes == "1":  # Listar todos os filmes
                print("Listar todos os filmes")

            elif opcao_filmes == "2":  # Listar um filme específico
                print("Listar um filme específico")

            elif opcao_filmes == "3":  # Incluir um filme
                print("Incluir um filme")

            elif opcao_filmes == "4":  # Alterar um filme
                print("Alterar um filme")

            elif opcao_filmes == "5":  # Excluir um filme
                print("Excluir um filme")

        elif opcao == "3":  # Submenu de Sessões
            submenu_sessoes()
            opcao_sessoes = input("Escolha uma opção: ")

            if opcao_sessoes == "1":  # Listar todas as sessões
                print("Listar todas as sessões")

            elif opcao_sessoes == "2":  # Listar uma sessão específica
                print("Listar uma sessão específica")

            elif opcao_sessoes == "3":  # Incluir uma sessão
                print("Incluir uma sessão")

            elif opcao_sessoes == "4":  # Alterar uma sessão
                print("Alterar uma sessão")

            elif opcao_sessoes == "5":  # Excluir uma sessão
                print("Excluir uma sessão")

        elif opcao == "4":  # Submenu de Relatórios
            submenu_relatorios()
            opcao_relatorios = input("Escolha uma opção: ")

            if opcao_relatorios == "a":  # Relatório de salas
                tipo_exibicao = input("Digite o tipo de exibição: ")
                capacidade_minima = int(input("Digite a capacidade mínima: "))
                relatorio_salas(salas, tipo_exibicao, capacidade_minima)

            elif opcao_relatorios == "b":  # Relatório de filmes
                ano_lancamento = int(input("Digite o ano de lançamento: "))
                relatorio_filmes(filmes, ano_lancamento)

            elif opcao_relatorios == "c":  # Relatório de sessões
                data_inicial = input("Digite a data inicial (formato: dd/mm/aaaa): ")
                data_final = input("Digite a data final (formato: dd/mm/aaaa): ")
                relatorio_sessoes(sessoes, data_inicial, data_final)

        elif opcao == "5":  # Sair
            break

        print()

if __name__ == "__main__":
    main()