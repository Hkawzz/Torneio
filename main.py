from entidades import usuario, adversarios
from caminho import inicio, boss_um

#recebendo dados
bosses = adversarios()
boss_fraco, boss_medio, boss_forte, boss_final = bosses
jogador = usuario()

#inicio
jogador = inicio(jogador)

#primeiro boss
boss_um(jogador, boss_fraco)