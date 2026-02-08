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
    escolha = trajetoria(
        lambda: pantano(jogador, boss),
        lambda: vulcao(jogador, boss),
        "inicial"
    )

    return escolha

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
    return "pantano"

def escolha_pantano(jogador, boss_um, boss_dois):
    print("Parabens, derrotou o primeiro inimigo pelo caminho do pantano")
    time.sleep(1)
    print()
    print("Agora deve fazer mais uma escolha, que pode facilitar, ou atrasar")
    print("Escolha bem...")
    time.sleep(1)
    print()
    trajetoria(
        lambda: esquerda_vulcao(jogador, boss_um),
        lambda: direita_vulcao(jogador, boss_dois),
        fase=None
            )

def esquerda_pantano(jogador, boss):
    print(jogador)
    print(boss)

def direita_pantano(jogador, boss):
    print(jogador)
    print(boss)

def ultimo_pantano(jogador, boss):
    primeira_escolha(jogador)
    print(boss)

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
    return "vulcao"
    
def escolha_vulcao(jogador, boss_um, boss_dois):
    print("Parabens, derrotou o primeiro inimigo pelo caminho do vulcão")
    time.sleep(1)
    print()
    print("Agora deve fazer mais uma escolha, que pode facilitar, ou atrasar")
    print("Escolha bem...")
    time.sleep(1)
    print()
    trajetoria(
        lambda: esquerda_vulcao(jogador, boss_um),
        lambda: direita_vulcao(jogador, boss_dois),
        fase=None
            )

def esquerda_vulcao(jogador, boss):
    print(jogador)
    print(boss)

def direita_vulcao(jogador, boss):
    print(jogador)
    print(boss)