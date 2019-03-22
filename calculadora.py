#Essa é uma calculadora simples de dois números
#Primeira operação funciona, as próximas ficam estranhas
num = []
valorf = 0
while True:
    #
    print('\nEscolha uma das opções abaixo.')
    print('Escreva \'som\' para somar dois números. ')
    print('Escreva \'sub\' para subtrair dois números. ')
    print('Escreva \'mul\' para multiplicar dois números. ')
    print('Escreva \'div\' para dividir dois números. ')
    print('Escreva \'fim\' para finalizar a aplicação. \n')
    opc = str(input('Sua escolha:'))
    num.clear()
    if opc == 'som':
        print('\nInforme os dois números a seguir: ')
        for i in range(2):
            num.append(float(input('Número ' + str(i+1) + ': ')))
            valorf += num[i]
        print(num[0], ' + ', num[1], ' = ', valorf,)
    elif opc == 'sub':
        print('\nInforme os dois números a seguir: ')
        for i in range(2):
            num.append(float(input('Número ' + str(i+1) + ': ')))
            valorf -= num[i]
        print(num[0], ' - ', num[1], ' = ', valorf,)
    elif opc == 'mul':
        print('\nInforme os dois números a seguir: ')
        for i in range(2):
            num.append(float(input('Número ' + str(i+1) + ': ')))
        valorf = num[0] * num[1]
        print(num[0], ' x ', num[1], ' = ', valorf,)
    elif opc == 'div':
        print('\nInforme os dois números a seguir: ')
        for i in range(2):
            num.append(float(input('Número ' + str(i+1) + ': ')))
        valorf = num[0] / num[1]
        print(num[0], ' / ', num[1], ' = ', valorf,)
    elif opc == 'fim':
        break
    else:
        print('\nOpção ' + opc + ' não existe, tente novamente.')

print('Aplicação finalizada com sucesso.')