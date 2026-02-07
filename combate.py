import random

def ataque_jogador(atk_jog, hp_boss):
    ataque = random.randint(1, atk_jog)
    hp_boss -= ataque
    if hp_boss >= 0:
        print("Você derrotou o boss")
    #ataque boss
    