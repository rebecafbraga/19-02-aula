def somar(a,b):
    resultado = (a + b)
    if resultado >= 40:
        print(resultado)
    else:
        print('ops, só retorno valores acima de 40')

    return resultado

a_input = float (input ('Digite um numero:'))
b_input = float (input ('Digite mais um numero:'))

somar(a_input, b_input)
