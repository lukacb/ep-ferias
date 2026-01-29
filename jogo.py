from funcoes import * 
import random

pecas = cria_pecas()
print("Bem-vindo(a) ao jogo de Dominó!")
num_jogadores = int(input("Quantos jogadores? (2-4) "))
jogo = inicia_jogo(num_jogadores, pecas)
jogador_atual = 0