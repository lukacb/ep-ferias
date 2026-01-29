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

def verifica_ganhador(jogadores):
    for jogador in jogadores:
        if len(jogadores[jogador]) == 0:
            return jogador
    return -1

def conta_pontos(pecas):
    total = 0
    for peca in pecas:
        total += peca[0] + peca[1]
    return total

def posicoes_possiveis(mesa, pecas):
    posicoes = []
    
    if len(mesa) == 0:
        for i in range(len(pecas)):
            posicoes.append(i)
        return posicoes
    
    ponta_esquerda = mesa[0][0]
    ponta_direita = mesa[-1][1]
    
    for i in range(len(pecas)):
        peca = pecas[i]
        if peca[0] == ponta_esquerda or peca[1] == ponta_esquerda or peca[0] == ponta_direita or peca[1] == ponta_direita:
            posicoes.append(i)
            
    return posicoes

def adiciona_na_mesa(peca, mesa):
    if len(mesa) == 0:
        return [peca]
    
    esquerda = mesa[0][0]
    direita = mesa[-1][1]
    
    if peca[0] == esquerda:
        mesa.insert(0, [peca[1], peca[0]])
        return mesa
    elif peca[1] == esquerda:
        mesa.insert(0, peca)
        return mesa
    elif peca[0] == direita:
        mesa.append(peca)
        return mesa
    elif peca[1] == direita:
        mesa.append([peca[1], peca[0]])
        return mesa
    
    return mesa

