"""
Uma classe é um modelo ou blueprint que descreve os atributos (variáveis) 
e comportamentos (métodos) comuns a um grupo de objetos relacionados. 

No contexto da orientação a objetos, uma classe funciona como uma base 
para criar instâncias, chamadas de objetos. Cada objeto criado a partir 
de uma classe possui os atributos e métodos definidos pela classe, 
mas com valores e estados específicos. 
"""

# Criar uma classe cliente   


#******************************************************************
class Cliente:

    def __init__(self, nome, cpf, email): 
        self._nome = nome
        self._cpf = cpf
        self._email = email


    def getnome(self):
        return self._nome 

cliente1 = Cliente('Léo', 123,'leo@gmail.com')
print(cliente1.getNome())

#*******************************************************************


class Funcionario:

    def __init__(self, nome, cpf, matricula):
        self._nome = nome
        self._cpf = cpf
        self._matricula = matricula

    def getnome(self):
        return self._nome
    
funcionario1 = Funcionario('Matheus', 12345, '0000')
print(funcionario1.getNome())










