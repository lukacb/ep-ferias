from funcoes import * 
import random

pecas = cria_pecas()
print("Bem-vindo(a) ao jogo de Dominó!")
num_jogadores = int(input("Quantos jogadores? (2-4) "))
jogo = inicia_jogo(num_jogadores, pecas)
jogador_atual = 0


while verifica_ganhador(jogo['jogadores']) == -1:
    print("\nMESA:")
    mesa_formatada = ""
    for p in jogo['mesa']:
        mesa_formatada += f"[{p[0]}|{p[1]}]"
    print(mesa_formatada if mesa_formatada else "Vazia")

    possiveis = posicoes_possiveis(jogo['mesa'], jogo['jogadores'][0])
    
    if jogador_atual == 0:
        print(f"Jogador: Você com {len(jogo['jogadores'][0])} peça(s)")
        mao = jogo['jogadores'][0]
        mao_str = ""
        for i in range(len(mao)):
            mao_str += f"[{mao[i][0]}|{mao[i][1]}] "
        print(mao_str)

        if len(possiveis) > 0:
            escolha = int(input(f"Escolha a peça (1-{len(mao)}): ")) - 1
            
            peca_valida = False
            for p_pos in possiveis:
                if escolha == p_pos:
                    peca_valida = True
            
            while not peca_valida:
                escolha = int(input("Inválido. Escolha outra: ")) - 1
                for p_pos in possiveis:
                    if escolha == p_pos:
                        peca_valida = True
            
            peca_escolhida = jogo['jogadores'][0].pop(escolha)
            jogo['mesa'] = adiciona_na_mesa(peca_escolhida, jogo['mesa'])
        else:
            if len(jogo['monte']) > 0:
                print("Sem peças! Pegando do monte...")
                jogo['jogadores'][0].append(jogo['monte'].pop(0))
            else:
                print("Passando a vez...")

    else:
        print(f"Jogador {jogador_atual + 1} com {len(jogo['jogadores'][jogador_atual])} peça(s)")
        possiveis_pc = posicoes_possiveis(jogo['mesa'], jogo['jogadores'][jogador_atual])
        
        if len(possiveis_pc) > 0:
            indice_peca = possiveis_pc[0]
            peca_pc = jogo['jogadores'][jogador_atual].pop(indice_peca)
            jogo['mesa'] = adiciona_na_mesa(peca_pc, jogo['mesa'])
            print(f"Colocou: [{peca_pc[0]}|{peca_pc[1]}]")
        elif len(jogo['monte']) > 0:
            jogo['jogadores'][jogador_atual].append(jogo['monte'].pop(0))
            print("Pegou do monte.")
        else:
            print("Passando a vez.")
            
    jogador_atual = (jogador_atual + 1) % num_jogadores

vencedor = verifica_ganhador(jogo['jogadores'])
if vencedor == 0:
    print("\nParabéns! Você venceu!")
else:
    print(f"\nFim de jogo! O Jogador {vencedor + 1} venceu.")