def upgrade(dados):
    while True:
        print("(1) HP")
        print("(2) Ataque")

        try:
            opcao = input("Escolha uma opção: ")
            opcao = int(opcao)

        except ValueError:
            print("Opção Inválida!")
            print("Tente Novamente")

        if opcao == 1:
            dados['hp'] += 5
            print("Upgrade para 45 HP")
            break

        elif opcao == 2:
            dados['atk'] += 5
            print("Upgrade para 35 de ataque")
            break
    return dados