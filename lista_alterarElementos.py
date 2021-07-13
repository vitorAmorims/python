#acesso o elemento pelo indice da lista
print(numeros[0]) # deve imprimir 1

#Indexação Negativa
# -1refere-se ao último item, -2refere-se ao penúltimo item etc.
print(numeros[-1])

#Gama de Índices
# Ao especificar um intervalo, o valor de retorno será uma nova lista com os itens especificados.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Ao omitir o valor inicial, o intervalo começará no primeiro item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


# Ao omitir o valor final, o intervalo irá para o final da lista:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Gama de índices negativos
# Especifique índices negativos se você deseja iniciar a pesquisa a partir do final da lista:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Verifique se o item existe
# Para determinar se um item especificado está presente em uma lista, use a inpalavra-chave:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Python - Alterar itens da lista
# Para alterar o valor de um item específico, consulte o número do índice:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Alterar um intervalo de valores de item
# Para alterar o valor dos itens em um intervalo específico, defina uma lista com os novos valores e consulte o intervalo de números de índice onde deseja inserir os novos valores:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
