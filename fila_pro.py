from collections import deque

class FilaPro:
    def __init__(self):
        # O deque é otimizado para adicionar e remover itens das pontas
        self.itens = deque()

    def entrar(self, nome):
        self.itens.append(nome) # Adiciona no fim
        print(f"{nome} chegou.")

    def atender(self):
        if self.itens:
            # remove o PRIMEIRO de forma super rápida
            return f"Atendendo agora: {self.itens.popleft()}" 
        return "Ninguém na fila."

# Testando
atendimento = FilaPro()
atendimento.entrar("Tamires")
atendimento.entrar("Alef")
print(atendimento.atender())
