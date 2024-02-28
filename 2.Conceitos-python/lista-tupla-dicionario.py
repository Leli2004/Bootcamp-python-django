#### Lista
lista = []
print(lista)
lista = ['um','dois','tres']
print(lista)
lista.append('quatro')
print(lista)
entrada = input('Digite um número por extenso: ')
lista.append(entrada)
print(lista)
lista[-1] # retorna o último valor da lista

#### Tupla
## são listas que não podem ser modificadas
tupla = ()
tupla = ('a','b','c')
print(tupla)

#### Dicionários
## associar valores a significados
# dicionario = {'chave':'valor'} 
# chave é o valor que referencia e o valor é a descrição
dicionario = {} 
dicionario['maca'] = 'É uma fruta'
dicionario['cachorro'] = 'É um animal'
dicionario['20'] = 'É um número'
print(dicionario)