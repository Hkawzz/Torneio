from combate import batalha
import time

def inicio(jogador):
    dados = jogador
    

    print("Bem vindo ao Jogo")
    time.sleep(1)
    nome = input("Qual o seu nome? ")
    print()

    print(f"Seja bem vindo(a) {nome}")
    time.sleep(1)

    print("Agora uma pequena ajuda antes de começar")
    print("Você tem 40 HP e um ataque máximo de 30")
    time.sleep(1)

    print("Escolha um para receber um upgrade de +5")
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

    print()
    print("Agora podemos seguir para o primeiro BOSS")
    print()
    time.sleep(1)
    return dados

def boss_um(jogador, boss):
    print("Chegamos ao primeiro boss")
    print("Derrote ele para avançar")
    print()
    time.sleep(1)
    resultado = batalha(jogador, boss)
    if resultado == "boss":
        return
    print("")