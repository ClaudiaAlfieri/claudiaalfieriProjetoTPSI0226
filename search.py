#Função par pesquisa_linear()

def pesquisa_linear(filmes, termo):
    resultados = []
    for filme in filmes:
        if termo.lower() in filme["titulo"].lower():
            resultados.append(filme)
    return resultados
