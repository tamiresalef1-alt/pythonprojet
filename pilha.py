class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)
        print(f"Adicionado: {item}")

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return "Erro: Pilha vazia!"

    def esta_vazia(self):
        return len(self.itens) == 0

# Testando a Pilha
p = Pilha()
p.empilhar("Livro 1")
p.empilhar("Livro 2")
print(f"Removido: {p.desempilhar()}")
