"""
Dicionários - Em outras linguagens, conhecido como MAPA.

Sintaxe
exemplo1 = {}
exemplo2 = dict()

Aceita qualquer tipo de dado.
As chaves não podem ser repetidas.
"""

tupla1 = () 
tupla2 = tuple()

lista1 = []
lista2 = list()

dicionario1={}

dicionario2=dict()


paises1= {'br' : 'Brasil'} 
paises2 = dict(br = 'Braisl') 

paises = dict( 
 br = 'Brasil',
 py = 'Paraguay' 
 ar = 'Argentina'
)
print(paises)
paises['br'] = 'matheus'
paises.update({'us': 'Estados unidos'})
print(paises) 

