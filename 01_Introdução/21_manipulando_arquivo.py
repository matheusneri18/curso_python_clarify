"""
Primeiro passo para leitura, é abrir o arquivo, para isto usamos
a função OPEN(nomeArquivo).
O parâmetro é o nome ou caminho do arquivo.

O arquivo deve existir, caso contrário retornará erro FileNotFound.

Open apenas abre o arquivo, para ler seu conteúdo é necessário usarmos
a função nomeArquivo.read()
Por padrão o Open abre com o parâmetro r(read)
"""

# criando um arquivo txt
# a -> adc w -> sub r -> leitura (pode ser suprimido)
# tratamento de erro

# Exercício de aula: criar um todo (lista de tarefas)

#*********************************************************************

# with open(' ./base/teste.txt', 'a', encoding = 'utf8') as arquivo:
#     arquivo.write('\nEstou só testando...') 
   

# with open('./baseteste.txt', 'w', encoding='utf8') as arquivo:
#     arquivo.write('estou testando, mas ja apaguei tudo')

# with open('./baseteste.txt', 'r', encoding='utf8') as arquivo:
#     print(arquivo)

# try: 
#     with open('comando git leo.txt', 'r', encoding ='utf8') as arquivo:
#         texto = arquivo.read()

# except FileNotFoundError:
#         print('Arquivo não Encontrado')

# except FileExistsError:
#     print('Arquivo não encontrado porque não existe')

# finally:
#      print('Volte Sempre')


#***********************************************************************


# def todo():
#     while True:
#         menu = int(input('1| Inserir\n2| visualizar\n3| Sair\nOpção: '))

#         match menu:
#          case 1:
#             try:  
                
#                 with open('to-do.txt', 'a', encoding='utf8') as arquivo :
#                     tarefa = str(input('digite uma tarefa:')) 
#                     arquivo.write(f'{tarefa}\n') 

#             except FileNotFoundError:
#                 print('Não encontrado...') 

# todo()


#*************************************************************


def todo():
   while True:
      
         menu = int(input('\n1| Inserir\n2| visualizar\n3| Sair\nOpção: '))
    
    
         match menu:
            case 1:
                try:
                    with open('./lista/to-do.txt', 'a', encoding='utf8') as arquivo:
        
                        while True:
                            tarefa = str(input('Digite uma tarefa ou S para sair:'))

                            if tarefa.lower() != 's':
                                arquivo.write(f'{tarefa}\n')
                            else:
                                break


                except FileNotFoundError:
                    print('Arquivo não foi encontrado')


       
            case 2:
                try:
                    with open('./lista/to-do.txt', 'a', encoding ='utf8') as arquivos:     
                        print(arquivo.read())

                except FileNotFoundError:
                    print('Não encontrado...')

            case 3:
                 break



todo()                    