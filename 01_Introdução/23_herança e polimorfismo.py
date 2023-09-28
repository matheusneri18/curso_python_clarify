"""  
HERANÇA é um tipo de relacionamento entre classes 
que significa que uma classe é outra.

POLIMORFISMO é a capacidade que uma subclasse tem de 
ter métodos com o mesmo nome de sua superclasse, e o 
programa saber qual método deve ser invocado, 
especificamente (da super ou sub). 
"""



#******************************************************************

class Pessoa:

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf


    def getNome(self):
        return self._nome


class Cliente(Pessoa):

    def __init__(self, nome, cpf, email): 
        super().__init__(nome, cpf)
        self._email = email


class Funcionario(Pessoa):

    def __init__(self, nome, cpf, matricula):
       Pessoa().__init__(nome, cpf)
       self._matricula = matricula

    def getnome(self):
        return[self._nome, self._matricula]



cliente1 = Cliente('Léo', 123,'leo@gmail.com')
print(cliente1.getNome())
    
funcionario1 = Funcionario('Matheus', 12345, '0000')
print(funcionario1.getNome())

