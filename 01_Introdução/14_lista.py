"""
Listas
Em outras linguagens é conhecida como Array, Vetor ou matriz...

* Dinâmica >>> Não possui tamanho fixo e não preciso informar este tamanho.
* Aceita qualquer tipo de dado.

* Sintaxe:
        [] ou list()

* SORT >>> Ordena os dados de uma lista.
* REVERSE >>> Inverte a lista.
* APPENDD >>> Atribui a lista, um elemento por vez. Podendo ser inclusive outra lista...
* INSERT >>> Atribui vários elementos, integrando à lista original.
* POP >>> Remove um valor da lista por índice.
* REMOVE >>> Remove um valor da lista por valor.
* ENUMERATE >>> Acesso à chave e valor.
* SHALLOW COPY
* CLEAR >>> Limpa a lista.
"""
tupla1 = () 
tupla2 = tuple() 

lista1 = [] 
lista2 = list() 

n10_1 = [range(0, 101, 10)] 
n10_2 = list(range(0,101, 10))

n10_3 = [10, 20, 30, 30, 30, 30, 'leo, True, 10.4']
print(n10_2)

#**********************************************************

notas =[] 

for n in range(4): 
        notas.append(float(input('Nota:')))


notas = [8, 5, 2, 10]
print (notas) 
notas.pop(2) #remove pelo indice
notas.remove(8)#remove pelo item
print (notas)

notas.append(4) #insere na ultima posição 
notas.insert(1, 15) # insere no indice que vc quiser
print(notas) 

print(8 in notas) 
 

notas = [8, 5, 20, 10]
for indice, item in enumerate(notas:)
        print(f'na posição{indice} temos a nota: item{item}') 