"""
Cadastre 3 produtos no estoque, cada produto precisa ter:
- nome
- preço
- data e hora que foi cadastrado
- Nome do Funcionário

Em seguida, permita que os produtos sejam visualizados.
"""

from datetime import datetime
estoque = []

 
while True : 
    menu = int(input('1 | Cadastrar\n2 | Vizualizar\n3 | Sair\nOpção:'))


    match menu:

        case 1:
            ...
            produto = dict( # Camisa Azul Camisa azul camisa azul
        nome =str(input('Nome:')).title(),
        preco =float(input('preço: R$ ')),
        nome_funcionario = str(input('Funcionários')).title(),
        dt_cadastro = datetime.now().strtime('%d.m%.%y | %H:%M')  
         )
            estoque.append(produto) 
       
        case 2: # Visualizando o estoque [{}, {}, {}, ]
            for i, p in enumerate(estoque):
                print(f'\nproduto: {i+1}')
            for c, v in p.items():
                print(f'{c}→{v}')
            print()

        case 3:
     
         break
       
        case _:
            print('Opção iválida')
        


