from data import carregar_config
from validate import validar_email, validar_password

#Login
def login():
    config = carregar_config()
    while True:
        while True:
            email = input("Digite seu email: ")
            if validar_email(email):
                break  
            else:
                print("Email inválido. Tente novamente.")
        
        while True:
            password = input("Digite sua password: ")
            if validar_password(password):
                break  
            else:
                print("Password inválida. Tente novamente.")

        if email == config["email"] and password == config["pass"]:
            return True
        else:
            print("Email ou password incorretos. Tente novamente.")