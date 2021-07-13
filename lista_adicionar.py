# Inserir itens
# O insert()método insere um item no índice especificado:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Para adicionar um item ao final da lista, use o método append () :
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List
# Para acrescentar elementos de outra lista à lista atual, use o extend()método.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Adicionar qualquer iterável
# O extend()método não precisa anexar listas , você pode adicionar qualquer objeto iterável (tuplas, conjuntos, dicionários etc.).
thislist = ["apple", "banana", "cherry"] #list
thistuple = ("kiwi", "orange") #tuple
thisdict = [{"Nome": "Vitor"}] #dict
thislist.extend(thistuple)
thislist.extend(thisdict)
print(thislist)

