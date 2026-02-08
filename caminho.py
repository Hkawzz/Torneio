from combate import batalha
from bonus import upgrade
from escolhas import trajetoria
import time

def inicio(jogador):
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
    dados = upgrade(jogador, boss=None)

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
        print("FIM DE JOGO!")
        return
    print("Agora com o primeiro boss derrotado")
    time.sleep(1)
    print()
    print("Você tem mais um upgrade")
    dados = upgrade(jogador, boss)

    return dados

def primeira_escolha(jogador, boss):
    time.sleep(1)
    print()
    print("Você deve escolher um caminho")
    trajetoria(
        lambda: pantano(jogador, boss),
        lambda: vulcao(jogador, boss),
        "inicial"
    )

def pantano(jogador, boss):
    print("Você escolheu o caminho do pantano")
    print("Agora podemos seguir para o seu próximo adversário")
    print()
    time.sleep(1)
    print("Ai está ele")
    print("Vamos a batalha")
    resultado = batalha(jogador, boss)
    if resultado == "boss":
        print("FIM DE JOGO!")
        return

def vulcao(jogador, boss):
    print("Você escolheu o caminho do vulcão")
    print("Agora podemos seguir para o seu próximo adversário")
    print()
    time.sleep(1)
    print("Ai está ele")
    print("Vamos a batalha")
    resultado = batalha(jogador, boss)
    if resultado == "boss":
        print("FIM DE JOGO!")
        return
    
def escolha_vulcao():
    print("Parabens, derrotou o primeiro inimigo pelo caminho do vulcão")