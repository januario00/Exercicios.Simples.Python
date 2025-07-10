numero = int(input('Digite o primeiro numero: '))
snumero = int(input('Digite o segundo numero: '))
operacao = str(input(' ** OPÇÕES ** \n 1- Soma \n 2- Subtração \n 3- Multiplicação \n 4- Divisão'
                     '\nQual operação você deseja fazer? '))
if operacao == '1':
    soma = numero + snumero
    print (soma)
elif operacao == '2':
    subtracao = numero - snumero
    print (subtracao)
elif operacao == '3':
    multiplicacao = numero * snumero
    print(multiplicacao)
elif operacao == '4':
    if snumero == 0: #Adição de um if dentro de um elif para verificar se o segundo numero é 0.
        print("Erro: Um numero dividido por zero é igual a ele mesmo.")
    else:
        divisao = numero / snumero
        print(divisao)
else:
    print ('Comando Inválido')