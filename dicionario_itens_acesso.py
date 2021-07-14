'''
Exemplo
Obtenha o valor da chave "model":
'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# Também existe um método chamado get()que fornecerá o mesmo resultado:

x = thisdict.get("model")
print(x)

# Obtenha uma lista das chaves:

x = thisdict.keys()
print(x)

# O values()método retornará uma lista de todos os valores do dicionário.
# Obtenha uma lista dos valores:
x = thisdict.values()
print(x)

# Adicione um novo item ao dicionário original e veja se a lista de chaves também é atualizada:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


'''
setdefault("color","white");
se não existir chave color e valor white, este método adiciona chave e valor no dicionário
'''
car.setdefault("color","white");
print(car)

'''
Obter itens
O items()método retornará cada item em um dicionário, como tuplas em uma lista.

Exemplo
Obtenha uma lista dos pares chave: valor
'''
x = thisdict.items()
print(x)

# Faça uma alteração no dicionário original e veja se a lista de itens também é atualizada:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change