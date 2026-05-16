from datetime import datetime


#Função que regista as logs do sistema.

def registar_log(mensagem):
    agora = datetime.now().strftime("%d-%m-%Y %H:%M")
    with open("logs.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(f"[{agora}] {mensagem}\n")
        
 
#Função para ver todos os logs 
        
def ver_logs():
    try:
        with open("logs.txt", "r", encoding="utf-8") as ficheiro:
            conteudo = ficheiro.read()
            if conteudo:
                print(conteudo)
            else:
                print("Nenhum log registado.")
    except FileNotFoundError:
        print("Nenhum log registado.")