"""
For >>> Utilizada quando se sabe a quantidade de repetições,
de forma que é obrigatório determinar o final da execução do laço.

Sintaxe:
for item in iteravel:
    bloco que será executado

* Range -> inicio, fim, passo
* Enumerate -> Permite acesso ao índice
"""

# sintaxe


#nome = 'Matheus'
# M a t h e u s
# 0 1 2 3 4 5 6 

soma = 0

for contador in range(5):
 print(soma)
 num = int(input('digite um numero:'))
#soma = soma + num 
soma += num

print (soma)

for  a in range( 10,21):

    print (a) 

inicio = 1
fim=6
from time import sleep
for cont in  range(1,6):
    print(cont) 
    sleep (2)


'''
Desafio de aula: Crie um sistema que receba 4 notas 
e calcule a média, ao fim apresente a média e situção
do aluno, sendo:
>7 aprovado, >5 em recuperação e <5 reprovado.
'''
#Resposta

# nota1= float(input('Digite a 1ºnota:'))
# nota2= float(input('Digite a 2ºnota:'))
# nota3= float(input('Digite a 3ºnota:'))
# nota4= float(input('Digite a 4ºnota:'))

# media = (nota1 +nota2 + nota3+ nota4) /4

# print(media)






nota = 0
for contador in range(1, 5):
    nota = float(input(f'digite a {contador}º nota:'))

if nota >0 and nota<= 10:

    media = nota + contador 

else: print('nota não tegistada')

print ('Nota não registrad')

media = nota / contador 
    # >7 aprovado, >5 em recuperação e <5 reprovado.