"""
IF, ELSE, ELIF
Permite que o código siga por caminhos diferentes
de acordo com resultado de análises, equações e etc.

Sintaxe:


if (teste):
    Bloco que será executado se o teste retornar True
"""

if 10 < 4: 

    print ('Ok, é maior')

'''
Exemplo de aplicação: 
Inserindo uma nota e testando as seguintes condições.
Se a nota for maior ou igual a 7 >>> O aluno está APROVADO.
Se a nota for menor que 7 e maior ou igual a 5 >>> o aluno está em RECUPERAÇÃO.
Se a nota for menor que 5 >>> o aluno está REPROVADO.
'''
#CONDIÇÃO SIMPLES

nota = 8.5 

# if nota >=7: 
#     print('Aluno Aprovado .')

# else:
#     print('Aluno Reprovado')

if nota >= 7: 
    print('Aluno aprovado.') 

elif nota >= 5: 
    print('Aluno em recuperação.')
  
else:
    print('Aluno Reprovado.')
 
# if nota >=5 and nota < 7:
#     print('Aluno em Recuperação')

# elif nota >= 7 and nota <= 10:
#print('Aluno aprovado')

# elif nota >=0 and nota < 5:
#   print('Aluno reprovado.')

# else:
#    print(Nota invalida) 



# Condição simples
# Condição composta
# Condição aninhada
''' Vamos criar um sistema para validadar se o cliente
pode ou não ter uma Habilitação de acordo com a idade 
que irá informar.
'''



idade = int(input('coloque sua idade:'))

if idade >=18 :
    print('voce pode dirigir.')



elif idade >=16 and idade <18:
    resp = str(input('tem autorização [s|n]:')).lower()


    if resp == 's':
        print('vamos continuar...')
    elif resp == 'n':
        print('não vamos continuar...')
    else: 
        print('Reposta invalida')



elif idade >= 0 and idade < 16:
    print('não vamos continuar' ) 

else :
    print('idade invalida') 



# Operadores unitários >>> Dependem de um único valor >>> not, is
# Operadores binários >>> Dependem de mais que 1 valor >>> and, or





