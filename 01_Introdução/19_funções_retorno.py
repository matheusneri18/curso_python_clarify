# Com retorno
# com mais de 1 retorno
# Desafio de aula: Cara ou Coroa
 

# def soma():
#     a = 10
#     b = 18
#     return a + b
#     print('só de teste')
#                         #somente com return (soma) é considerado  28
#     print(soma() * 10) 


#*****************************************************************8

# from random import random, randint

# print(random()) #entre 1 e 0
# print(randint(1, 10))

# def teste():
#     dado = 1
#     if dado >=5:
#         return 'é maior que 5'
#     return 'é menor q 5'

#********************************************************

#desafio cara ou coroa

from random import random, randint 


def CaraCoroa():

    if randint(1,2) == 1:       #COMO SERIA FAZENDO POR RANDINT
        ...

    if random () >= 0.5:        #COMO SERIA FAZENDO POR RANDOM
        return 'Cara'
    return 'Coroa'

print(CaraCoroa())