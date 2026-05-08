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

# Função que mostra o total de filmes por tipo

def total_por_tipo(filmes):
    if len(filmes) == 0:
        print("Nenhum filme registado.")
        return
    total_filmes = 0
    total_series = 0
    for filme in filmes:
        if filme["tipo"] == "filme":
            total_filmes += 1            
        elif filme["tipo"] == "série":
            total_series += 1            
    print(f"Total de filmes: {total_filmes}")  
    print(f"Total de séries: {total_series}")
    
# Função que filtra os filmes por plataforma ou género

def filtrar_filmes(filmes):
    if len(filmes) == 0:
        print("Nenhum filme registado.")
        return
    print("1. Filtrar por plataforma")
    print("2. Filtrar por género")
    opcao = input("Escolha: ")
    resultados = []
    if opcao == "1":
        termo = input("Plataforma: ")
        for filme in filmes:
            if termo.lower() in filme["plataforma"].lower():
                resultados.append(filme)                
    elif opcao == "2":    
        termo = input("Género: ")
        for filme in filmes:
            if termo.lower() in filme["genero"].lower():
                resultados.append(filme) 
    if not resultados:
        print("Nenhum filme encontrado.")
    else:
        ver_filmes(resultados)
           
    
    

