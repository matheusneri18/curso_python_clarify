"""
 Faça um programa que leia ano de nascimento de 5 pessoas e no final
 mostre quantas pessoas já atingiram a maioridade e para aquelas que
 ainda atingiram, mostre a média em anos que faltam para chegarem a maior idade.
"""

from datetime import date 

ano_atual = date.today(). year
qtd_maior = qtd_menor= 0 
qtd_maior = qtd_menor = soma_menor=0


for cont in range(5): 
    ano_nasc= int(input('Digite ano de nascimento:')) 

    if (ano_atual - ano_nasc) >=18: 
        qtd_maior += 1
        print('Mais uma pessoa maior da idade..\n') 
    
    else: 
        qtd_menor +=1
        soma_menor += 18 - (ano_atual - ano_nasc) 

media = soma_menor / qtd_menor


#*******************************************************************