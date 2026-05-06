#Função par pesquisa_linear()

def pesquisa_linear(filmes, termo):
    resultados = []
    for filme in filmes:
        if termo.lower() in filme["titulo"].lower():
            resultados.append(filme)
    return resultados


#Função par pesquisa_binaria()

def pesquisa_binaria(filmes, ano):
    esquerda = 0
    direita = len(filmes) - 1
    while (esquerda <= direita):
        meio = (esquerda + direita) // 2
        if filmes[meio]["ano"] == ano:
            return [filmes[meio]]
        elif filmes[meio]["ano"] < ano:
            esquerda = meio + 1
        elif filmes[meio]["ano"] > ano:
            direita = meio - 1
    return []