#Validação de email utilizando regex (email deve ter o formato nome@dominio.com)

import re

def validar_email(email):
    padrao = r"\w+@\w+\.\w+$"
    if re.match(padrao, email):
        return True
    return False

# validação de senha utilizando regex (senha deve conter pelo menos 8 caracteres, pelo menos 1 letra maiúscula, e pelo menos 1 número)

def validar_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):  
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True

