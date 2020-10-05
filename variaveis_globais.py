#Variáveis ​​globais podem ser usadas por qualquer pessoa, tanto dentro quanto fora das funções.
x = 'awesome' #variable global

def myFunc():
    x = 'fantastic'
    print('Python is '+ x) #concatenção de string + string da variavel global

myFunc() #chamando função

#Se você criar uma variável com o mesmo nome dentro de uma função, essa variável será local e só pode ser usada dentro da função.

'''
ormalmente, quando você cria uma variável dentro de uma função, essa variável é local e só pode ser usada dentro dessa função.

Para criar uma variável global dentro de uma função, você pode usar a globalpalavra - chave.
'''
def praise():
    global God
    God = 'wonderful'
    print(God)
praise() #chamei função

print('My God is: ' + God) # aqui estou chamando a variavel global que foi criada dentro de uma função.

