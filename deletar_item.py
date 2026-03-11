from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from banco_dados import Historico

# 1. Conecta no banco
engine = create_engine('sqlite:///meu_projeto.db')
Session = sessionmaker(bind=engine)
session = Session()

# 2. Pergunta qual ID deletar
id_para_deletar = input("Digite o ID do item que deseja apagar: ")

# 3. Busca o item no banco
item = session.query(Historico).filter(Historico.id == id_para_deletar).first()

if item:
    session.delete(item)
    session.commit()
    print(f"Sucesso! O item com ID {id_para_deletar} foi removido.")
else:
    print("ID não encontrado no banco.")

session.close()
