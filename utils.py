import os
from datetime import datetime

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_data(data_str):
    try:
        return datetime.strptime(data_str, "%d/%m/%Y").date()
    except ValueError:
        return None
