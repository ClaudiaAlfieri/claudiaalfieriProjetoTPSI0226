#Função para receber a lista de filmes e mostrar no ecrã

def ver_filmes(filmes):
    for filme in filmes:
        print("----------------------------")
        print(f"ID: {filme['id']}")
        print(f"Título: {filme['titulo']}")
        print(f"Tipo: {filme['tipo']}")
        print(f"Género: {filme['genero']}")
        print(f"Ano: {filme['ano']}")
        print(f"Plataforma: {filme['plataforma']}")
        print(f"Nota: {filme['nota']}")
        print(f"Data de visualização: {filme['data_visualizacao']}")
        print(f"Comentário: {filme['comentario']}")
        print("----------------------------")
        
#Função para adicionar um filme

def adicionar_filme(filmes):
    if len(filmes) == 0:
        novo_id = 1
    else:
        novo_id = filmes[-1]["id"] + 1
    titulo = input("Título: ")
    tipo = input("Tipo: ")
    genero = input("Género: ")
    ano = input("Ano: ")
    plataforma = input("Plataforma: ")
    nota = input("Nota: ")
    while True:
        data = input("Data de visualização (DD-MM-AAAA): ")
        if validar_data(data):
            break
        else:
            print("Data inválida. Tente novamente.")
    comentario = input("Comentário: ")
    
    novo_filme = {
    "id": novo_id,
    "titulo": titulo,
    "tipo": tipo,
    "genero": genero,
    "ano": ano,
    "plataforma": plataforma,
    "nota": nota,
    "data_visualizacao": data,
    "comentario": comentario    
    }
    
    filmes.append(novo_filme)
    return filmes