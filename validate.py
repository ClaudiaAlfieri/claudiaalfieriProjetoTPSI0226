#Validação de email utilizando regex (email deve ter o formato nome@dominio.com)

import re

def validar_email(email):
    padrao = r"\w+@\w+\.\w+$"
    if re.match(padrao, email):
        return True
    return False

