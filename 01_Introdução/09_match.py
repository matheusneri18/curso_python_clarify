"""
Estrutura condicionais mais utilizada em menus,
funciona semelhante ao escolhaCaso do portugol
e switch case no java por exemplo...
"""
# Calculadora

''' 
Conclua o exemplo inserindo: 
    multiplicar, dividir e resto da divisão.
'''

menu = int(input('[1]SOMAR\n[2]SUBTRAIR\n[3]MULTIPLICAR\n[4]Dividir\nOpção:')) 

if menu >=1 and menu <=4:

    num1 = int(input('Digite um numero:'))
    num2 = int(input('Digite um numero:'))


match menu:
    case 1:
        print (f'resultado: {num1 + num2}')

    case 2:
        print(f'resultado{num1 - num2}')
  
    case 3:
        print(f'resultado{num1 * num2}')
   
    case 4:
        print(f'resultado{num1 / num2}') 

    case _:
        print('opção inválida') 