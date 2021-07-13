# ordem crescente
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#ordem decrescente
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Função de classificação personalizada
# Classifique a lista com base na proximidade do número de 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# Classificação que não diferencia maiúsculas de minúsculas
# Por padrão, o sort()método diferencia maiúsculas de minúsculas, resultando em todas as letras maiúsculas classificadas antes das minúsculas:

# A classificação com distinção entre maiúsculas e minúsculas pode dar um resultado inesperado:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


# Portanto, se você quiser uma função de classificação que não diferencia maiúsculas de minúsculas, use str.lower como uma função-chave:

# Exemplo
# Faça uma classificação da lista sem distinção entre maiúsculas e minúsculas:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)