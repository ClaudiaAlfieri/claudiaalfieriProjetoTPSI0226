from data import carregar_filmes, guardar_filmes
from auth import login
from menus import mostrar_menu
from filmes import ver_filmes, adicionar_filme, apagar_filme, editar_filme
from search import pesquisar_filme
from sort import ordenar_filme
from estatisticas import mostrar_estatisticas

filmes = []

if login():
    filmes = carregar_filmes()


while True:
    opcao = mostrar_menu()
    if opcao == "1":
        ver_filmes(filmes)
    elif opcao == "2":
        filmes = adicionar_filme(filmes)
    elif opcao == "3":
        filmes = editar_filme(filmes)
    elif opcao == "4":
        filmes = apagar_filme(filmes)
    elif opcao == "5":
        pesquisar_filme(filmes)            
    elif opcao == "6":
        guardar_filmes(filmes)
        print("Dados guardados com sucesso!")
    elif opcao == "7":
        filmes = ordenar_filme(filmes)
    elif opcao == "8":
        mostrar_estatisticas(filmes)
    elif opcao == "9":
        salvar = input("Deseja guardar (S/N)? ").upper()
        if salvar == "S":
            guardar_filmes(filmes)
            break
        else:
            break