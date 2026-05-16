#Função para mostrar o menu no ecrã e pedir ao utilizador para escolher uma opção.

def mostrar_menu():   
    print()
    print("==========================================") 
    print(r"""
     _____         ______  _  _       
    |  __ \       |  ____|| |(_)      
    | |__) |_   _ | |__   | | _ __  __
    |  ___/| | | ||  __|  | || |\ \/ /
    | |    | |_| || |     | || | >  < 
    |_|     \__, ||_|     |_||_|/_/\_\
            __/ |                    
            |___/                     
    """)
    print("==========================================") 
    print("           1. Ver lista de filmes")
    print("           2. Adicionar filme")
    print("           3. Editar")
    print("           4. Apagar")
    print("           5. Pesquisar")
    print("           6. Guardar")
    print("           7. Ordenar")
    print("           8. Estatísticas")
    print("           9. Exportar filmes")
    print("           10. Ver logs")
    print("           11. Sair")
    print("==========================================")     
    opcao = input("Escolha uma opção: ")
    return opcao
