from validate import validar_data
from logs import registar_log

#Função para receber a lista de filmes e mostrar no ecrã

def ver_filmes(filmes):
    print()
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
    print("Tipo:")
    print("1. Filme")
    print("2. Série")
    tipo_opcao = input("Escolha: ")
    if tipo_opcao == "1":
        tipo = "filme"
    elif tipo_opcao == "2":
        tipo = "série"
    else:
        print("Opção inválida.")
        return filmes
    genero = input("Género: ")
    ano = int(input("Ano: "))
    plataforma = input("Plataforma: ")
    nota = float(input("Nota: "))
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
    registar_log(f"Filme adicionado: {titulo}")
    return filmes

#Função para apagar filmes

def apagar_filme(filmes):
    filme_apagar = int(input("Id do filme que deseja apagar: "))
    for filme in filmes:
        if filme["id"] == filme_apagar:
            ver_filmes([filme])
            confirmacao = input("Tens a certeza? (S/N): ").upper()
            if confirmacao == "S":
                filmes.remove(filme)
                registar_log(f"Filme apagado: ID {filme_apagar}")
                print("Filme apagado!")
            else:
                print("Operação cancelada.")
            return filmes
    print("Filme não encontrado.")    
    return filmes
            
#Função para editar filmes

def editar_filme(filmes):
    filme_id = int(input("Id do filme que deseja editar: "))
    for filme in filmes:
        if filme["id"] == filme_id:
            ver_filmes([filme])
            print("1. Título")           
            print("2. Tipo")            
            print("3. Género")           
            print("4. Ano")         
            print("5. Plataforma")           
            print("6. Nota")            
            print("7. Data da visualização")       
            print("8. Comentário")
           
            editar = input("Qual campo deseja editar? ")
            if editar == "1":
                novo_valor = input("Novo título: ")
                filme["titulo"] = novo_valor
            elif editar == "2":
                novo_valor = input("Novo tipo: ")
                filme["tipo"] = novo_valor
            elif editar == "3":
                novo_valor = input("Novo género: ")
                filme["genero"] = novo_valor
            elif editar == "4":
                novo_valor = input("Novo ano: ")
                filme["ano"] = novo_valor
            elif editar == "5":
                novo_valor = input("Nova plataforma: ")
                filme["plataforma"] = novo_valor
            elif editar == "6":
                novo_valor = input("Nova nota: ")
                filme["nota"] = novo_valor
            elif editar == "7":
                while True:
                    novo_valor = input("Nova data (DD-MM-AAAA): ")
                    if validar_data(novo_valor):
                        filme["data_visualizacao"] = novo_valor
                        break
                    else:
                        print("Data inválida. Tente novamente.")  
            elif editar == "8":
                novo_valor = input("Novo comentário: ")
                filme["comentario"] = novo_valor   
            registar_log(f"Filme editado: ID {filme_id}")                
            return filmes
    print("Filme não encontrado.")   
    return filmes