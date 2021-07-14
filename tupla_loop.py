'''
Exemplo
Repita os itens e imprima os valores:
'''

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

'''
Exemplo
Imprima todos os itens referindo-se ao seu número de índice:
'''

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

'''
Exemplo
Imprima todos os itens, usando um whileloop para percorrer todos os números do índice:
'''

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

