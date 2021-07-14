# Remover itens
'''
Exemplo
Converta a tupla em uma lista, remova "apple" e converta-a novamente em uma tupla:
'''

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

'''
Exemplo
A delpalavra-chave pode excluir a tupla completamente:
'''
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists