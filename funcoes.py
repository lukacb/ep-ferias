from random import shuffle

def cria_pecas():
    pecas = []
    
    for i in range(7):
        for j in range(i, 7):
            pecas.append([i, j])
    
    shuffle(pecas)
    
    return pecas

def inicia_jogo(num_jogadores, pecas):
    pecas_copia = pecas.copy()
    jogadores = {}
    
    for i in range(num_jogadores):
        jogadores[i] = []
        for _ in range(7):
            jogadores[i].append(pecas_copia.pop())
    jogo = {
        'jogadores': jogadores,
        'monte': pecas_copia,
        'mesa': []
    }
    
    return jogo

