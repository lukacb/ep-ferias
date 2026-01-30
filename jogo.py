from funcoes import * 
import random

pecas = cria_pecas()
print("Bem-vindo(a) ao jogo de Dominó!")
num_jogadores = int(input("Quantos jogadores? (2-4) "))
jogo = inicia_jogo(num_jogadores, pecas)
jogador_atual = 0


jogando = True
while jogando:
    print("\nMESA:")
    mesa_formatada = ""
    for p in jogo['mesa']:
        mesa_formatada += f"[{p[0]}|{p[1]}]"
    print(mesa_formatada if mesa_formatada else "Vazia")

    if jogador_atual == 0:
        print(f"Jogador: Você com {len(jogo['jogadores'][0])} peça(s)")
        mao_str = ""
        mao = jogo['jogadores'][0]
        for i in range(len(mao)):
            p = mao[i]
            mao_str += f"[{p[0]}|{p[1]}] "
        print(mao_str)
    
    
    jogando = False