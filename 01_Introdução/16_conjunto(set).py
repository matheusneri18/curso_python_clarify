# Sets

# tupla1 = ()
# tupla2 = tuple()                #indice e item

# lista1 = []
# lista2 = list()

# dicionario1 = {}                # chave e valor
# dicionario2 = dict()

# conjunto1 = {'Léo', 10, 10.4, True} #não aceita valor repetido
# conjunto2 = set()


# numeros = {6,4,8,9,4,6,1,3,2}

# numeros.add(200) 

# numeros.pop()
# numeros.discard(4)
# print(numeros )

#*************************************************************************


# Analise cidades (cada pessoa que entrou colocou a cidade de nascimento)
cidade = ['Rio de Janeiro', 'São Paulo', 'Juiz de Fora', 'Petrolina',
          'Salvador','Juiz de Fora', 'Rio de Janeiro', 'Petrolina',
          'Salvador', 'São Paulo', 'São Paulo', 'São Paulo',  'Juiz de Fora',
          'Rio de Janeiro', 'Petrolina', 'Rio de Janeiro', 'Salvador',
          'Juiz de Fora',  'Petrolina', 'Salvador', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro', 'São Paulo',
          'São Paulo', 'São Paulo', 'São Paulo', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro',  'São Paulo', 'Rio de Janeiro',
          'São Paulo', 'Rio de Janeiro', 'São Paulo']
#******************************************************************************

# #Total de pessoas:
# print(f'Total de pessoas: {len(cidade)}')

# #Quantas pessoas são do Rio de Janeiro
# print(f'total de pessoas do Rj: {cidade.count("Rio de Janeiro")}')

# # De quasis cidades eu recebi pessoas hoje:
# print(f'Quantidade de cidades: {len(set(cidade))}') 
# print(f'Cidades: {set(cidade)}')


#**********************************************************************

curso_python ={'Leo A', 'MAria', 'Juca,''Paulo','Ana', 'Beto'}
curso_sql = {'leo A', 'Pedro', 'Juca', 'Cris', 'Claudia', 'Roberta'}

#Total de alunos 

print(f'QTD alunos PY {len(curso_python)}')
print(f'QTD alunos PY {len(curso_sql)}')

total_alunos1 = curso_python.union(curso_sql)
total_alunos2 = curso_python  | curso_sql
 
print(f'Total de alunos: {len(total_alunos1)}')



#Alunos matriculados nos 2 cursos

ambos_cursos1 = curso_python.intersection(curso_sql)
ambos_cursos2 = curso_python & curso_sql

# Alunos que estão em apenas um curso
so_python= curso_python.difference(curso_sql)
so_sql = curso_sql ^ curso_python


print(f'QTD alunos PY......:{len(curso_python)}')
print(f'QTD alunos SQL.....:{len(curso_sql)}')
print(f'total de alunos....:{len(total_alunos1)}')
print(f'Aluno nos 2 cursos.:{len(ambos_cursos2)}')
print(f'alunos só em Python:{len(so_python)}')
print(f'Alunos só em SQL...:{len(so_sql)}')