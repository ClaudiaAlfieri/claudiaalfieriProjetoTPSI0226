# Função para calcular a média das notas

def media_notas(filmes):
    if len(filmes) == 0:
        print("Nenhum filme registado.")
        return
    total = 0
    for filme in filmes:
        total += filme["nota"]
    media = total / len(filmes)
    return media

# Função para verificar a nota mais alta e mais baixa

def nota_maxima_minima(filmes):
    if len(filmes) == 0:
        print("Nenhum filme registado.")
        return
    maior = filmes[0]
    menor = filmes[0]
    for filme in filmes:
        if filme["nota"] > maior["nota"]:
            maior = filme
        if filme["nota"] < menor["nota"]:
            menor = filme
    return maior, menor