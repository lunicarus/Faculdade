# Funções do submenu de salas
def submenu_salas():
    salas = {}
    while True:
        print("\nSubmenu de Salas:")
        print("1. Listar todas as salas")
        print("2. Listar uma sala específica")
        print("3. Incluir uma nova sala")
        print("4. Alterar os dados de uma sala")
        print("5. Excluir uma sala")
        print("6. Voltar ao menu principal")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            listar_salas(salas)
        elif opcao == "2":
            codigo = input("Digite o código da sala: ")
            listar_sala_especifica(salas, codigo)
        elif opcao == "3":
            incluir_sala(salas)
        elif opcao == "4":
            codigo = input("Digite o código da sala: ")
            alterar_sala(salas, codigo)
        elif opcao == "5":
            codigo = input("Digite o código da sala: ")
            excluir_sala(salas, codigo)
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Digite novamente.")

# Funções do submenu de filmes
def submenu_filmes():
    filmes = {}
    while True:
        print("\nSubmenu de Filmes:")
        print("1. Listar todos os filmes")
        print("2. Listar um filme específico")
        print("3. Incluir um novo filme")
        print("4. Alterar os dados de um filme")
        print("5. Excluir um filme")
        print("6. Voltar ao menu principal")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            listar_filmes(filmes)
        elif opcao == "2":
            codigo = input("Digite o código do filme: ")
            listar_filme_especifico(filmes, codigo)
        elif opcao == "3":
            incluir_filme(filmes)
        elif opcao == "4":
            codigo = input("Digite o código do filme: ")
            alterar_filme(filmes, codigo)
        elif opcao == "5":
            codigo = input("Digite o código do filme: ")
            excluir_filme(filmes, codigo)
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Digite novamente.")

# Funções do submenu de sessões
def submenu_sessoes():
    sessoes = {}
    while True:
        print("\nSubmenu de Sessões:")
        print("1. Listar todas as sessões")
        print("2. Listar uma sessão específica")
        print("3. Incluir uma nova sessão")
        print("4. Alterar os dados de uma sessão")
        print("5. Excluir uma sessão")
        print("6. Voltar ao menu principal")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            listar_sessoes(sessoes)
        elif opcao == "2":
            codigo_filme = input("Digite o código do filme: ")
            codigo_sala = input("Digite o código da sala: ")
            data = input("Digite a data da sessão (formato: DD/MM/AAAA): ")
            horario = input("Digite o horário da sessão (formato: HH:MM): ")
            listar_sessao_especifica(sessoes, codigo_filme, codigo_sala, data, horario)
        elif opcao == "3":
            incluir_sessao(sessoes)
        elif opcao == "4":
            codigo_filme = input("Digite o código do filme: ")
            codigo_sala = input("Digite o código da sala: ")
            data = input("Digite a data da sessão (formato: DD/MM/AAAA): ")
            horario = input("Digite o horário da sessão (formato: HH:MM): ")
            alterar_sessao(sessoes, codigo_filme, codigo_sala, data, horario)
        elif opcao == "5":
            codigo_filme = input("Digite o código do filme: ")
            codigo_sala = input("Digite o código da sala: ")
            data = input("Digite a data da sessão (formato: DD/MM/AAAA): ")
            horario = input("Digite o horário da sessão (formato: HH:MM): ")
            excluir_sessao(sessoes, codigo_filme, codigo_sala, data, horario)
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Digite novamente.")

# Função principal do programa
def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Submenu de Salas")
        print("2. Submenu de Filmes")
        print("3. Submenu de Sessões")
        print("4. Submenu Relatórios")
        print("5. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            submenu_salas()
        elif opcao == "2":
            submenu_filmes()
        elif opcao == "3":
            submenu_sessoes()
        elif opcao == "4":
            # Implementar submenu de relatórios
            print("Submenu de relatórios em construção.")
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Digite novamente.")

# Execução do programa
if __name__ == "__main__":
    main()
