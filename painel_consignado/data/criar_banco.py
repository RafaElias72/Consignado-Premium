import sqlite3 
import os 

print("Criando o banco de dados")

caminho_banco = r"C:\Users\Rafael\Desktop\painel_consignado\data\banco.db"

pasta = os.path.dirname(caminho_banco)
if not os.path.exists(pasta):
    os.makedirs(pasta)
    
    print(f"Pasta criada: {pasta}")
else:
    print(f"Pasta já existe: {pasta}")

conn = sqlite3.connect(caminho_banco)
cursor = conn.cursor()

cursor.execute
(
    """
    CREATE TABLE IF NOT EXISTS Consignado 
    (
        ID_Registro INTEGER PRIMARY KEY AUTOINCREMENT,
        Codigo TEXT,
        Nome_Peca TEXT,
        Chamado TEXT,
        CaseID_Consig TEXT,
        CaseID_Troca TEXT,
        Tecnico TEXT,
        Data TEXT,
        OBS TEXT
    )
    """
)

conn.commit()
conn.close()

print(f"Banco de dados criado com sucesso {caminho_banco}")