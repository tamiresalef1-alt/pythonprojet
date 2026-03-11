import customtkinter as ctk
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# --- BANCO DE DADOS ---
Base = declarative_base()
engine = create_engine('sqlite:///meu_projeto.db')
Session = sessionmaker(bind=engine)
session = Session()

class Historico(Base):
    __tablename__ = 'historico'
    id = Column(Integer, primary_key=True)
    acao = Column(String)

Base.metadata.create_all(engine)

# --- INTERFACE ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema CRUD Python - Tamires Dev")
        self.geometry("500x600")

        self.label = ctk.CTkLabel(self, text="Gerenciador de Itens", font=("Arial", 22, "bold"))
        self.label.pack(pady=20)

        # Entrada para ADICIONAR
        self.entry = ctk.CTkEntry(self, placeholder_text="Digite o novo item...", width=350)
        self.entry.pack(pady=10)

        self.btn_add = ctk.CTkButton(self, text="➕ SALVAR NO BANCO", command=self.salvar_no_banco, fg_color="green", hover_color="#006400")
        self.btn_add.pack(pady=5)

        # Entrada para DELETAR
        self.entry_del = ctk.CTkEntry(self, placeholder_text="Digite o ID para apagar...", width=150)
        self.entry_del.pack(pady=(20, 5))

        self.btn_del = ctk.CTkButton(self, text="🗑️ APAGAR POR ID", command=self.deletar_do_banco, fg_color="#B22222", hover_color="#8B0000")
        self.btn_del.pack(pady=5)

        # Lista de Itens
        self.textbox = ctk.CTkTextbox(self, width=420, height=250, font=("Consolas", 12))
        self.textbox.pack(pady=20)

        self.carregar_dados()

    def salvar_no_banco(self):
        texto = self.entry.get()
        if texto:
            novo = Historico(acao=texto)
            session.add(novo)
            session.commit()
            self.entry.delete(0, 'end')
            self.carregar_dados()

    def deletar_do_banco(self):
        id_input = self.entry_del.get()
        if id_input.isdigit():
            item = session.query(Historico).filter(Historico.id == int(id_input)).first()
            if item:
                session.delete(item)
                session.commit()
                self.entry_del.delete(0, 'end')
                self.carregar_dados()

    def carregar_dados(self):
        self.textbox.delete("1.0", "end")
        itens = session.query(Historico).all()
        for i in itens:
            self.textbox.insert("end", f" ID: {i.id} | Item: {i.acao}\n")

if __name__ == "__main__":
    app = App()
    app.mainloop()
