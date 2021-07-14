'''
Mudar valores
Você pode alterar o valor de um item específico, referindo-se ao seu nome de chave:

Exemplo
Altere o "ano" para 2018:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

# Atualize o "ano" do carro usando o update() método:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# método setdefault("color","white"), se nao existir chave e valor ele adiciona 
thisdict.setdefault("color","white")
print(thisdict)

