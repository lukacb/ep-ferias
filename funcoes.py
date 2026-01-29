from random import shuffle

def cria_pecas():
    pecas = []
    
    for i in range(7):
        for j in range(i, 7):
            pecas.append([i, j])
    
    shuffle(pecas)
    
    return pecas

def inicia_jogo(n_jogadores, pecas):
    distribuicao = {}
    posicao = 0
    
    for i in range(n_jogadores):
        mao = pecas[posicao : posicao + 7]
        distribuicao[i] = mao
        posicao += 7
        
    monte = pecas[posicao:]
    
    resultado = {
        'jogadores': distribuicao,
        'monte': monte,
        'mesa': []
    }
    
    return resultado

