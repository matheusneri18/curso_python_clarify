"""
While com Break
while True: >>> este laço será executado enquanto 
não encontrar o Break pelo caminho.
Break >>> Condição de parada de um loop. (FLAG)
"""
# sintaxe
# Validando tipo de dado com break




while True: 
    menu = int(input('[1]somar\n[2] subtrair\n[3]sair\opção:')) 

    if menu == 1 or menu ==2: 
        n1 = int(input('valor 1:'))
        n2 = int(input('valor 2 :')) 


    match menu: 
        case 1:print(f'Resultado da adição:{n1 + n2}')
        case 2:print(f'resulltado da subtração: {n1 - n2}')
        case 3: break
        case _: print('Opção inválida...\n')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
#*****************************************************************************************




