"""
    Remaking last calculator but using functions
"""

#4 functions for the basic operations
def som(x, y):
    z = x + y
    return z

def sub(x, y):
    z = x - y
    return z

def mult(x, y):
    z = x * y
    return z

def div(x, y):
    z = x / y
    return z

#Menu options
#Math operations are in portuguese and all program output
#
while True:
    print('Digite "som" para somar.')
    print('Digite "sub" para subtrair.')
    print('Digite "mult" para multiplicar.')
    print('Digite "div" para dividir.')
    print('Digite "fim" para finalizar a aplicação')
    op = str(input('Escolha uma das operações: \n'))
    if op == 'som':
        print('Informe dois números para realizar a soma: ')
        x = float(input('Primeiro número: '))
        y = float(input('Segundo número: '))
        print(som(x, y), '\n')
    elif op == 'sub':
        print('Informe dois números para realizar a subtração: ')
        x = float(input('Primeiro número: '))
        y = float(input('Segundo número: '))
        print(sub(x, y), '\n')
    elif op == 'mult':
        print('Informe dois números para realizar a multiplicação: ')
        x = float(input('Primeiro número: '))
        y = float(input('Segundo número: '))
        print(mult(x, y), '\n')
    elif op == 'div':
        print('Informe dois números para realizar a divisão: ')
        x = float(input('Primeiro número: '))
        y = float(input('Segundo número: '))
        print(div(x, y), '\n')
    elif op == 'fim':
        #the program will finish
        break
    else:
        print('Valor inválido, digite novamente.\n')

print('\nPrograma finalizado com sucesso.')

