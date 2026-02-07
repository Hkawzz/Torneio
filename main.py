from entidades import usuario, vilao
import random

#recebendo dados
bosses = vilao()
boss_fraco, boss_medio, boss_forte, boss_final = bosses

jogador = usuario()
jog_hp = jogador['hp']
jog_atk = jogador['atk']

print("ataque do jogador")
input("aperte qualquer tecla para atacar")
ataque = random.randint(0, jog_atk)
print(ataque)