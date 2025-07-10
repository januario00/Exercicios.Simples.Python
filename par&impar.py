

quantidade = int(input("Quantos numeros você gostaria de informar?"))
for i in range (quantidade):
    numero = int(input('Qual numero?'))
    if numero %2 == 0:
        print ('O numero {} é par'.format(numero))
    else:
        print ('O numero {} é impar'.format(numero))