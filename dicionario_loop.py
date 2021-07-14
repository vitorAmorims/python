
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)

# Imprima todos os valores do dicionário, um por um:
for x in thisdict:
  print(thisdict[x])

# Você também pode usar o values()método para retornar valores de um dicionário:
for x in thisdict.values():
  print(x)

# Você pode usar o keys()método para retornar as chaves de um dicionário:
for x in thisdict.keys():
  print(x)

# Loop através de chaves e valores , usando o items()método:
for x, y in thisdict.items():
  print(x, y)
