from data import carregar_filmes, guardar_filmes
from auth import login

filmes = []

if login():
    filmes = carregar_filmes()
       