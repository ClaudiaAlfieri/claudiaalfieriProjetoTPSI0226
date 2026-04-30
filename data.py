import json

#Função para carregar os filmes do ficheiro JSON
def carregar_filmes():    
    try:
        with open("filmes.json", "r") as ficheiro:
            filmes = json.load(ficheiro)
            return filmes
    except FileNotFoundError:
        return []
    
#Função para guardar os filmes no ficheiro JSON
def guardar_filmes(filmes):    
    try:
        with open("filmes.json", "w") as ficheiro:
            json.dump(filmes, ficheiro)
    except (PermissionError, IOError):
        print("Erro ao guardar os dados.")
        
#Função para carregar o ficheiro JSON
def carregar_config():
    try:
        with open("config.json", "r") as ficheiro:
            config = json.load(ficheiro)
            return config
    except FileNotFoundError:
        print("Erro: ficheiro config.json não encontrado.")
        exit()