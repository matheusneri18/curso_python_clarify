"""
Tuplas >>> Tuple

Tuplas não são mutáveis, uma vez criada, permanecerá tal qual durante do o código.
- Aceita assim como as listas, quaisquer tipos de dados.

Sintaxe's
variável = ()
variável = tuple()

Tuplas são definidas por , e não por uso de parenteses.

Métodos de adição, remoção, alteração, ordenação em tuplas não existem.

Utilizamos em coleções que não sofrem alterações.
"""

# Criando uma tupla

tupla1= () 
tupla2= tuple() 

tupla3= ('leo', 30,1.83,True) 

meses_anos= ('janeiro', 'feveiro', 'março') 
meses_anos = ('leo', 'juca') 
usuarios = 'leo', 'maria', 'juca'


for pessoa in usuarios:
    print(f'boa tarde:{pessoa}') 

numeros = (10,9,6,4,8,6,5,7) 

print(sum(numeros))
print(max(numeros)) 
print(min(numeros)) 


#*****************************************************************