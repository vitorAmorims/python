# Percorrer uma lista
# Você pode percorrer os itens da lista usando um for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Percorrer os números de índice
# Você também pode percorrer os itens da lista referindo-se ao seu número de índice.

# Use as funções range()e len()para criar um iterável adequado.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#   Usando um While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping usando compreensão de lista
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

