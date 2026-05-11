from datetime import datetime


#Função que regista as logs do sistema.

def registar_log(mensagem):
    agora = datetime.now().strftime("%d-%m-%Y %H:%M")
    with open("logs.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(f"[{agora}] {mensagem}\n")