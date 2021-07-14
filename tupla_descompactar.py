'''
Exemplo
Descompactando uma tupla:
'''

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green) #print apple
print(yellow) #print banana
print(red) #print cherry

'''
Exemplo
Atribua o restante dos valores como uma lista chamada "vermelho":
'''

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) #apple
print(yellow) #banana
print(red) #print list ['cherry', 'strawberry', 'raspberry']

'''
Se o asterisco for adicionado a outro nome de variável diferente do último, o Python atribuirá valores à variável até que o número de valores restantes corresponda ao número de variáveis ​​restantes.

Exemplo
Adicione uma lista de valores à variável "tropic":
'''

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic) # print new list ['mango', 'papaya', 'pineapple']
print(red)

