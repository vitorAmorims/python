#Variáveis ​​globais podem ser usadas por qualquer pessoa, tanto dentro quanto fora das funções.
x = 'awesome' #variable global

def myFunc():
    print('Python is '+ x) #concatenção de string + string da variavel global

myFunc() #chamando função
