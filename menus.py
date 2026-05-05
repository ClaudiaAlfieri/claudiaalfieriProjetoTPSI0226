#Função para mostrar o menu no ecrã e pedir ao utilizador para escolher uma opção.

def mostrar_menu():   
    print("========== PyFlix ==========")
    print("1. Ver lista de filmes")
    print("2. Adicionar filme")
    print("3. Editar filme")
    print("4. Apagar filme")
    print("5. Pesquisar filme")
    print("6. Guardar dados")
    print("7. Sair")
    print("============================")     
    opcao = input("Escolha uma opção: ")
    return opcao
