import random
import time

def batalha(jogador, boss):
    atk_jog = jogador['atk']
    hp_jog = jogador['hp']
    atk_boss = boss['atk']
    hp_boss = boss['hp']

    while hp_jog > 0 and hp_boss > 0:
        #ataque jogador
        input("Aperte qualquer tecla para atacar: ")
        time.sleep(1)
        ataque_jogador = random.randint(5, atk_jog)
        hp_boss -= ataque_jogador

        if hp_boss <= 0:
            print(f"Você deu {ataque_jogador} de ataque")
            print("Boss derrotado, Parabens!")
            resultado = "jogador"
            return resultado
        
        time.sleep(1)
        print()
        print(f"O boss ficou com {hp_boss} de hp")
        time.sleep(1)
        print(f"Se prepare para o ataque dele")
        print()
        time.sleep(1)
        
        #ataque boss
        ataque_boss = random.randint(1, atk_boss)
        hp_jog -= ataque_boss

        if hp_jog <= 0:
            print(f"Você recebeu {ataque_boss} de ataque")
            print("Você foi derrotado!")
            resultado = "boss"
            return resultado
        
        print(f"Você recebeu {ataque_boss} de ataque")
        print(f"E ficou com {hp_jog} HP")
        print()
        print("Sua vez de atacar!")

        