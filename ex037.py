import math
from time import sleep

numero = int(input('Digite um numero inteiro para a conversão: '))

print ('MENU')
print ('1 - Binário \n2 - Octal \n3 - Hexadecimal')

while True:
    conversao = int(input('Escolha sua forma de conversão: '))
    if conversao == 1:
        print(bin(numero))
    elif conversao == 2:
        print(oct(numero))
    elif conversao == 3:
        print(hex(numero))
    else:
        print("Numero digitado fora da cartela de escolha")
    sleep(2)


