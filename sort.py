#Função que faz o Bubble Sort que ordena comparando dois elementos adjacentes da lista e fazendo a troca deles.

def bubble_sort(filmes, campo):
    n = len(filmes)
    for i in range(n):
        for j in range(0, n-i-1):
            if filmes[j][campo] > filmes[j+1][campo]:
                # troca os dois elementos
                filmes[j], filmes[j+1] = filmes[j+1], filmes[j]
    return filmes