from entidades import usuario, adversarios
from caminho import inicio, boss_um, primeira_escolha
import time

#recebendo dados
bosses = adversarios()
boss_fraco, boss_medio, boss_forte, boss_final = bosses
jogador = usuario()

#inicio
jogador = inicio(jogador)

#primeiro boss
resultado = boss_um(jogador, boss_fraco)

#após escolher a direção
jogador = primeira_escolha(jogador, boss_medio)