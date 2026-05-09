from filmes import ver_filmes

#Função que ordena comparando dois elementos vizinhos na lista e fazendo a troca deles.

def bubble_sort(filmes, campo):
    n = len(filmes)
    for i in range(n):
        for j in range(0, n-i-1):
            if filmes[j][campo] > filmes[j+1][campo]:
                # troca os dois elementos
                filmes[j], filmes[j+1] = filmes[j+1], filmes[j]
    return filmes

#Função que ordena procurando o menor elementa da lista e colocando na primeira posição.

def selection_sort(filmes, campo):
    n = len(filmes)
    for i in range(n):
        menor = i
        for j in range(i+1, n):
            if filmes[j][campo] < filmes[menor][campo]:
                menor = j
        filmes[i], filmes[menor] = filmes[menor], filmes[i]
    return filmes

#Função que coordena os dois tipos de ordenação (Bubble Sort e Selection Sort).

def ordenar_filme(filmes):
    print("Campos disponíveis:")
    print("1. ano")
    print("2. nota")
    print("3. titulo")  
    campo = input("Escolha o campo: ")
    if campo == "1":
        campo = "ano"
    elif campo == "2":
        campo = "nota"
    elif campo == "3":
        campo = "titulo"
    ordem = input("Ordem (C-Crescente / D-Decrescente): ").upper()   
    print("1. Ordenar por Bubble Sort (compara e troca elementos vizinhos)")
    print("2. Ordenar por Selection Sort (procura o menor e coloca no início)")
    opcao = input("Escolha: ")       
    if opcao == "1":
        resultados = bubble_sort(filmes, campo)
    elif opcao == "2":
        resultados = selection_sort(filmes, campo)
    if ordem == "D":
        resultados.reverse()
    ver_filmes(resultados)
    return filmes