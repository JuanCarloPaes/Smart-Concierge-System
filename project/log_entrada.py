import os
from datetime import datetime

# Diretório e arquivo para o log
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "entrada_log.txt")

# Função para registrar logs
def registrar_entrada(tipo, nome):
    """Registra o log de entrada."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{data_hora}] Tipo: {tipo} | Nome: {nome}\n"
    
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)

    print("Entrada registrada:", log_entry)
