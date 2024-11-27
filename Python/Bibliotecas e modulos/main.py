from funcoes import adicao,subtracao,multiplicacao,divisao


def menu(operacao):

    if operacao == '+':

        print(f'O resultado da sua operação é: {adicao(numero1,numero2)}')


    elif operacao == '-':

        print(f'O resultado da sua operação é: {subtracao(numero1,numero2)}')


    elif operacao == '*':

        print(f'O resultado da sua operação é: {multiplicacao(numero1,numero2)}')


    elif operacao == '/':

        print(f'O resultado da sua operação é: {divisao(numero1,numero2)}')


print('CALCULADORA \n adição(+) \n subtração(-) \n multiplicação(*) \n divisão(/) \n Sair(Q)')


while True:

    operacao = input('Digite o tipo de operação')

    if operacao == 'Q':

        break

    numero1 = int(input('Digite o primeiro número da operação'))

    numero2 = int(input('Digite o segundo número da operação'))

    menu(operacao)



















