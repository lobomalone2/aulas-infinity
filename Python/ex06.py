def celsius_para_fahrenheit(celsius: float):
    calculo = (celsius * 9/5) + 32
    return calculo


temp_celsius = float(input('digite a temperatura a ser convertida'))

resultado = celsius_para_fahrenheit(temp_celsius)

print(f'O resultado convertido de:{temp_celsius} é {resultado} °')


