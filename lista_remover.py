# Python - Remover itens da lista
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remover Índice Especificado
# O pop()método remove o índice especificado.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Se você não especificar o índice, o pop()método remove o último item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# A del palavra-chave também remove o índice especificado:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Limpe a lista
# O clear()método esvazia a lista.

# A lista ainda permanece, mas não tem conteúdo

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
