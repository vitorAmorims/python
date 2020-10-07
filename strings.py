# Em Python 3 tudo é objeto e uma string é do tipo str.

x = 'hello' #aspas simples
# print(x)
x = "hello" #aspas duplas
# print(x)
x = '''loremçlkslçklçskldkslkls #use três aspas simples, para escrever entre as linhas.
dçssflsf]fruits
sçsdds'''
# print(x)

#strings são arrays
nome = "vitor"
# print(nome[4]) #exemplo, estou acessando ultimo caracter da variavel nome

#podemos acessar uma string pelo seu index
# print(nome[0])

#Mas não podemos alterar seu valor atribuindo um valor através do índice.
# nome[0] = 1 

#http://devfuria.com.br/python/strings/

#string é um objeto iterável.
for palavra in 'nome':
    print palavra

#Fatiamento
# print(nome[2:4])

#length
# print(len(nome)) #metodo length len(nome_da_variavel) para obter o tamanho da string

'''
métodos para string
strip()
'''

