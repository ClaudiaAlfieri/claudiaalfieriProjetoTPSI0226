from filmes import ver_filmes
from sort import bubble_sort

#Função para pesquisa_linear()

def pesquisa_linear(filmes, termo):
    resultados = []
    for filme in filmes:
        if termo.lower() in filme["titulo"].lower():
            resultados.append(filme)
    return resultados


#Função para pesquisa_binaria()

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

#Função para coordenar os dois tipos de pesquisa (linear e binaria)

def pesquisar_filme(filmes):
    print("1. Pesquisa por título (linear)")
    print("2. Pesquisa por ano (binária)")
    opcao = input("Escolha: ")   
    if opcao == "1":
        termo = input("Título a pesquisar: ")
        resultados = pesquisa_linear(filmes, termo)
        if not resultados:
            print("Nenhum filme encontrado.")
        else:
            ver_filmes(resultados)
    elif opcao == "2":        
        filmes = bubble_sort(filmes, "ano")
        ano = int(input("Ano a pesquisar: "))
        resultados = pesquisa_binaria(filmes, ano)
        if not resultados:
            print("Nenhum filme encontrado.")
        else:
            ver_filmes(resultados)
        
        