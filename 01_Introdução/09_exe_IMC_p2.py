"""
Agora vamos finalizar o IMC gerando uma saída
personalizada para o usuário de acordo com a
tabela:
______________________________________________
| Menor que 18.5      | Abaixo do peso       |
| Entre 18.5 - 24.9   | Peso Normal          |
| Entre 25.0 - 29.9   | Excesso de peso      |
| Entre 30.0 - 34.9   | Obesidade classe I   |
| Entre 35.0 - 39.9   | Obesidade classe II  |
| Maior ou igual 40.0 | Obesidade classe III |
----------------------------------------------

Mostre também a data deste resultado.
"""

nome = str(input('Digite seu nome:')).title()
idade = int(input(f'{nome},agora sua idade:'))
peso = float(input('Peso:'))
altura = float(input('altura:'))

imc=float(peso/altura**2)

if imc< 18.5:
  print('voce esta abaixo do peso')

elif imc>=30 and imc<=40:
         print('voce esta obeso')  

elif imc >=30 and imc <=34.9: 
    print('voce tem obesidade class 1')

elif imc>=35.0 and imc <=39.9:
    print('voce tem obesidade classe 2')

elif imc>= 40 :
    print('voce tem obesidade classe 3')
    
elif imc>=25.0 and imc<=29.9: 
    print('voce esta com excesso de peso')

else :
     print('resultado invalido') 