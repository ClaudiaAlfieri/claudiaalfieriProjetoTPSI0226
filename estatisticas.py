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