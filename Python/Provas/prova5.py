def maior_numero(n1,n2,n3):
    
    if n1 > n2 and n1 > n2:
        return print(f'O maior numero é: {n1}')
    elif n2 > n1 and n2 > n3:
        return print(f'O maior numero é: {n2}')
    elif n3 > n1 and n3 > n2:
        return  print(f'O maior numero é: {n3}')
    elif n1 == n2 and n1 == n3:
        return print(f'Os numeros são iguais')

    
numero1 = int(input('Digite o numero 1'))
numero2 = int(input('Digite o numero 2'))
numero3 = int(input('Digite o numero 3'))

 
maior_numero(numero1,numero2,numero3)