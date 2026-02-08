def upgrade(dados, boss):
    while True:
        print("(1) HP")
        print("(2) Ataque")

        try:
            opcao = input("Escolha uma opção: ")
            opcao = int(opcao)

        except ValueError:
            print("Opção Inválida!")
            print("Tente Novamente")
            continue

        if boss is None:
            n = 5

        elif boss['nome'] == "boss_fraco":
            n = 5
        
        elif boss['nome'] == "boss_medio":
            n = 10

        else:
            n = 15

        if opcao == 1:
            dados['hp'] += n
            print(f"Upgrade para {dados['hp']} HP")
            break

        elif opcao == 2:
            dados['atk'] += n
            print(f"Upgrade para {dados['atk']} de ataque")
            break

        else:
            print("Opção inválida!")
    return dados