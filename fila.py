class Fila:
    def __init__(self):
        self.itens = []

    def entrar_na_fila(self, nome):
        self.itens.append(nome)
        print(f"{nome} entrou na fila.")

    def atender(self):
        if len(self.itens) > 0:
            # remove o PRIMEIRO item (índice 0)
            atendido = self.itens.pop(0) 
            return f"Atendendo: {atendido}"
        return "Fila vazia!"

# Testando a Fila
f = Fila()
f.entrar_na_fila("Cliente A")
f.entrar_na_fila("Cliente B")
print(f.atender()) # Deve atender o Cliente A
print(f.atender()) # Deve atender o Cliente B
