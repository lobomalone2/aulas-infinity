def string_vazia(texto):

    if texto == '':
        boleano = True

    else:
        
        boleano = False
    
    return boleano


text = input('Digite algo para false e nada para true')

resultado = string_vazia(text)

print(resultado)


