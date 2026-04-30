import json

#Função para carregar os filmes do ficheiro JSON
def carregar_filmes():    
    try:
        with open("filmes.json", "r") as ficheiro:
            filmes = json.load(ficheiro)
            return filmes
    except FileNotFoundError:
        return []
    
