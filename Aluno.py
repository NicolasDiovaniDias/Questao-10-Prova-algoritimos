from Pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self, id, nome, _cpf, __matricula):
        super().__init__(id, nome, _cpf)
        self.__matricula = __matricula

    def get__matricula(self):
        return self.__matricula
    
    def set__matricula(self, __matricula):
        self.__matricula = __matricula
    
    def marcarPresenca(self):
        print(f"{self.nome} esta com a presença marcada!")
        
    def __str__(self):
        return super().__str__() + f"\nmatricula = {self.__matricula}"
    
    def imprimir(self):
        print(self)

    
