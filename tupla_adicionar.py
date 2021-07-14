'''
Coleções Python (matrizes)
Existem quatro tipos de dados de coleção na linguagem de programação Python:

  Lista é uma coleção ordenada e mutável. Permite membros duplicados.

  Tupla é uma coleção ordenada e imutável. Permite membros duplicados.

  Set é uma coleção não ordenada e não indexada. Sem membros duplicados.

  O dicionário é uma coleção ordenada * e mutável. Sem membros duplicados.
  
* A partir da versão 3.7 do Python, os dicionários são solicitados . No Python 3.6 e anteriores, os dicionários não são ordenados .
'''


'''
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
'''

# Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

'''
Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
'''

'''
Example
Tuples allow duplicate values:
'''

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

