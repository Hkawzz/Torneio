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
    escolha, dados = trajetoria(
        lambda: pantano(jogador, boss),
        lambda: vulcao(jogador, boss),
        "inicial"
    )

    return escolha, dados

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
    time.sleep(1)
    print()
    print("Você tem mais um upgrade")
    dados = upgrade(jogador, boss)
    return "pantano", dados

def escolha_pantano(jogador, boss_um, boss_dois, ultimo_boss):
    print("Parabens, derrotou o primeiro inimigo pelo caminho do pantano")
    time.sleep(1)
    print()
    print("Agora deve fazer mais uma escolha, que pode facilitar, ou atrasar")
    print("Escolha bem...")
    time.sleep(1)
    print()
    trajetoria(
        lambda: esquerda_pantano(jogador, boss_um, ultimo_boss),
        lambda: direita_pantano(jogador, boss_dois, ultimo_boss),
        fase=None
            )

def esquerda_pantano(jogador, boss, ultimo_boss):
    print("Seguindo pelo caminho escolhido")
    print("Chegamos a mais um adversário")
    print()
    print("Você está chegando no final, derrote ele e continue")
    print()
    time.sleep(1)
    resultado = batalha(jogador, boss)
    if resultado == "boss":
        print("FIM DE JOGO!")
        return
    time.sleep(1)
    print()
    print("Você tem mais um upgrade")
    jogador = upgrade(jogador, boss)
    ultimo_pantano(jogador, ultimo_boss)

def direita_pantano(jogador, boss, ultimo_boss):
    print("Seguindo pelo caminho escolhido")
    print("Chegamos a mais um adversário")
    print()
    print("Você se deu bem, pegou um boss fraco")
    print("Mas ainda tem um caminho até o ultimo, derrote e continue")
    print()
    time.sleep(1)
    resultado = batalha(jogador, boss)
    if resultado == "boss":
        print("FIM DE JOGO!")
        return
    time.sleep(1)
    print()
    print("Você tem mais um upgrade")
    jogador = upgrade(jogador, boss)
    ultimo_pantano(jogador, ultimo_boss)

def ultimo_pantano(jogador, boss):
    print("Você chegou ao ultimo adversário do pantano")
    print("Derrote ele e volte ao caminho original")
    time.sleep(1)
    print()
    resultado = batalha(jogador, boss)
    if resultado == "boss":
        print("FIM DE JOGO!")
        return
    print(jogador)

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
    time.sleep(1)
    print()
    print("Você tem mais um upgrade")
    dados = upgrade(jogador, boss)
    return "vulcao", dados
    
def escolha_vulcao(jogador, boss_um, boss_dois, ultimo_boss, final_boss):
    print("Parabens, derrotou o primeiro inimigo pelo caminho do vulcão")
    time.sleep(1)
    print()
    print("Agora deve fazer mais uma escolha, que pode facilitar, ou atrasar")
    print("Escolha bem...")
    time.sleep(1)
    print()
    trajetoria(
        lambda: esquerda_vulcao(jogador, boss_um, final_boss),
        lambda: direita_vulcao(jogador, boss_dois, ultimo_boss, final_boss),
        fase=None
            )

def esquerda_vulcao(jogador, boss, final_boss):
    print("Seguindo pelo caminho escolhido")
    print("Chegamos a mais um adversário")
    print()
    print("E você fez uma otima escolha")
    print("Derrote esse adversario e chegue direto ao ultimo")
    print()
    time.sleep(1)
    resultado = batalha(jogador, boss)
    if resultado == "boss":
        print("FIM DE JOGO!")
        return
    time.sleep(1)
    print()
    print("Você tem mais um upgrade")
    jogador = upgrade(jogador, boss)
    boss_final(jogador, final_boss)

def direita_vulcao(jogador, boss, ultimo_boss, final_boss):
    print("Seguindo pelo caminho escolhido")
    print("Chegamos a mais um adversário")
    print()
    print("Você está chegando no final, derrote ele e continue")
    print()
    time.sleep(1)
    resultado = batalha(jogador, boss)
    if resultado == "boss":
        print("FIM DE JOGO!")
        return
    time.sleep(1)
    print()
    print("Você tem mais um upgrade")
    jogador = upgrade(jogador, boss)
    ultimo_boss(jogador, ultimo_boss, final_boss)

def ultimo_vulcao(jogador, boss, final_boss):
    print("Você chegou ao ultimo adversário do vulcao")
    print("Derrote ele e volte ao caminho original")
    time.sleep(1)
    print()
    resultado = batalha(jogador, boss)
    if resultado == "boss":
        print("FIM DE JOGO!")
        return
    time.sleep(1)
    print()
    print("Você tem mais um upgrade")
    jogador = upgrade(jogador, boss)
    boss_final(jogador, final_boss)

def boss_final(jogador, boss):
    resultado = batalha(jogador, boss)
    print("fim")
    if resultado == "boss":
        print("FIM DE JOGO!")
        return