from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Configuração do Banco (Cria o arquivo meu_projeto.db)
Base = declarative_base()
engine = create_engine('sqlite:///meu_projeto.db')
Session = sessionmaker(bind=engine)
session = Session()

# 2. Definição da Tabela (Sua Estrutura de Dados no Banco)
class Historico(Base):
    __tablename__ = 'historico'
    id = Column(Integer, primary_key=True)
    acao = Column(String)

# 3. Cria a tabela de verdade
Base.metadata.create_all(engine)

# 4. Salvando um dado (Simulando uma Pilha)
nova_acao = Historico(acao="Livro 1 adicionado na Pilha")
session.add(nova_acao)
session.commit()

print("Sucesso! O arquivo 'meu_projeto.db' foi criado e o dado foi salvo.")
