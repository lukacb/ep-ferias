from random import shuffle

def cria_pecas():
    pecas = []
    
    for i in range(7):
        for j in range(i, 7):
            pecas.append([i, j])
    
    shuffle(pecas)
    
    return pecas
