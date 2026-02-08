def trajetoria(caminho_a, caminho_b, fase):
    while True:
        if fase == "inicial":
            print("(1) Caminho do Pantano")
            print("(2) Caminho do Vulcão")

        else:
            print("(1) Lado Esquerdo")
            print("(2) Lado Direito")

        try:
            opcao = input("Escolha sua direção: ")
            opcao = int(opcao)

        except ValueError:
            print("Opção Inválida!")
            print("Tente Novamente")

        if opcao == 1:
            return caminho_a()

        elif opcao == 2:
            return caminho_b()