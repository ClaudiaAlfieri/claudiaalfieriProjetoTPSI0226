#Função que faz o Bubble Sort que ordena comparando dois elementos vizinhos na lista e fazendo a troca deles.

def bubble_sort(filmes, campo):
    n = len(filmes)
    for i in range(n):
        for j in range(0, n-i-1):
            if filmes[j][campo] > filmes[j+1][campo]:
                # troca os dois elementos
                filmes[j], filmes[j+1] = filmes[j+1], filmes[j]
    return filmes

#Função Selection Sort que ordena procurando o menor elementa da lista e colocando na primeira posição.

def selection_sort(filmes, campo):
    n = len(filmes)
    for i in range(n):
        menor = i
        for j in range(i+1, n):
            if filmes[j][campo] < filmes[menor][campo]:
                menor = j
        filmes[i], filmes[menor] = filmes[menor], filmes[i]
    return filmes