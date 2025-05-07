from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, id, nome, _cpf):
        self.id = id
        self.nome = nome
        self._cpf = _cpf
        
    def __str__(self):
        return f"id = {self.id}\nnome = {self.nome}\ncpf = {self._cpf}"
    def imprimir(self):
        print(self)

    @abstractmethod
    def marcarPresenca(self):
        pass