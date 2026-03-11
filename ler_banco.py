from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from banco_dados import Historico, Base # Importa a estrutura que você já criou

# 1. Conecta no banco existente
engine = create_engine('sqlite:///meu_projeto.db')
Session = sessionmaker(bind=engine)
session = Session()

# 2. Busca TODOS os registros da tabela Historico
todas_as_acoes = session.query(Historico).all()

print("--- HISTÓRICO DE AÇÕES NO BANCO ---")
if not todas_as_acoes:
    print("O banco está vazio.")
else:
    for item in todas_as_acoes:
        print(f"ID: {item.id} | Ação: {item.acao}")

session.close()
