#Variáveis ​​globais podem ser usadas por qualquer pessoa, tanto dentro quanto fora das funções.
x = 'awesome' #variable global

def myFunc():
    x = 'fantastic'
    print('Python is '+ x) #concatenção de string + string da variavel global

myFunc() #chamando função

#Se você criar uma variável com o mesmo nome dentro de uma função, essa variável será local e só pode ser usada dentro da função.

