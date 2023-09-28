"""
While >>> Utilizada quando se sabe a quantidade de repetições e
quando não se sabe.
* Necessário atentar para o critério de parada.

Sintaxe >>>  while expressão_bool:
                    Execução.

Expressão será executada enquanto for verdadeira.
Expressão Booleana >>> Toda expressão onde o resultado
for Verdadeiro ou Falso.

Ex.
resposta = ''
    while resposta != 'SIM':
            resposta = 'input'

            




"""

# repetindo um texto 5 vezes com for
# repetindo um texto 5 vezes com while
# validando uma senha de forma simples

#**************************************************************

# senha_cadastrada = str(input('cadastre uma senha:')).lower()

# while senha != senha_cadastrada:
#     senha = str(input('Digite uma senha para entrar: ')).lower()
# if senha !=senha_cadastrada:

#     print('\033[31\nAcesso permitido...\033[m') 

# print('\033[32m\nAcesso permitido...\033[m') 


#*********************************************************************

qtd_notas=1
soma_notas=0
while True:
    nota = float(input(f'Digite a {qtd_notas +1}ª nota:')) 

    if nota >=0 and nota <= 10:
        qtd_notas += 1
        soma_notas += nota 
    else:
        print('Nota invalida... digite novamente...')

    if qtd_notas==4:
        break

print(f'média: {round(soma_notas / qtd_notas,1)}')

#**********************************************************************

