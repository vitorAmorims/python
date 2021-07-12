'''
Python tem os seguintes tipos de dados integrados por padrão, nestas categorias:

Tipo de texto:	str
Tipos numéricos:	int, float, complex
Tipos de sequência:	list, tuple, range
Tipo de mapeamento:	dict
Tipos de conjuntos:	set, frozenset
Tipo booleano:	bool
Tipos binários:	bytes, bytearray, memoryview
'''

# Você pode obter o tipo de dados de qualquer objeto usando a type()função:

x = 5
print(type(x)) # x is int

x = '5'
print(type(x)) # x is string

x = 5.1
print(type(x)) # x is float

numeros = [1,2,3,4,5]
print(type(numeros)) # numeros is list

# numeros = (1,2,3,4,5)
print(type(numeros)) # numeros is tuple

# numeros = {1,2,3,4,5}
print(type(numeros)) # numeros is set

# car = ({"car","house"})
print(type({"car","house"}))

texto = '10'
num = int(texto) # conversão para inteiro
print(num)
print(texto + str(texto)) # conversão para string

# #Vetores, Matrizes e Conjuntos
# '''
# Python possui dois tipos de listas a do tipo list e a do tipo tuple. E qual a diferença entre um e outro?

# Uma tupla é uma lista imutável. Então, você nunca consegue alterar o seu conteúdo.

# Essa diferença fica clara quando você olha os métodos que uma lista e uma tupla possui.

# list:

# append, count, extend, index, insert, pop, remove, reverse, sort.
# tuple:

# count, index.
# '''
fruits = ['banana', 'pera','uva','abacate']
print('size of fruits: ', len(fruits))

