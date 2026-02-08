from entidades import usuario, adversarios
from caminho import inicio, boss_um, primeira_escolha, escolha_vulcao, escolha_pantano
import time

def main():
    #recebendo dados
    bosses = adversarios()
    boss_fraco, boss_medio, boss_forte, boss_final = bosses
    jogador = usuario()

    #inicio
    jogador = inicio(jogador)

    #primeiro boss
    resultado = boss_um(jogador, boss_fraco)

    #após escolher a direção
    escolha = primeira_escolha(jogador, boss_medio)
    if escolha == "vulcao":
        escolha_vulcao(jogador, boss_forte, boss_medio)
    else:
        escolha_pantano(jogador, boss_medio, boss_fraco)

if __name__ == "__main__":
    main()