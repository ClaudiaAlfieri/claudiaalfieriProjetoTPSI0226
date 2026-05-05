from data import carregar_filmes, guardar_filmes
from auth import login
from menus import mostrar_menu

filmes = []

if login():
    filmes = carregar_filmes()


while True:
    opcao = mostrar_menu()
    if opcao == "1":
        ver_filmes()
    elif opcao == "2":
        adicionar_filme()
    elif opcao == "3":
        editar_filme()
    elif opcao == "4":
        apagar_filme()
    elif opcao == "5":
        pesquisar_filme()
    elif opcao == "6":
        guardar_dados()
    elif opcao == "7":
        salvar = input("Deseja guardar (S/N)? ")
        if salvar == "S":
            guardar_filmes(filmes)
            break
        else:
            break