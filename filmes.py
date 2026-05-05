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