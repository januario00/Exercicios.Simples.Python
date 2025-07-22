from datetime import date
from time import sleep


print('='*20)
print ('    ALISTAMENTO')
print('='*20)

print('\nLEIA COM ATENÇÃO')
print('Informações adicionais, para que o alistamento seja realizado:\n\n'
      '👦 Quem deve se alistar?\n'
      '- Homens brasileiros, natos ou naturalizados (ou por opção), devem se alistar no ano em que completam 18 anos.\n'
      '- Brasileiros naturalizados ou por opção têm 30 dias a partir da data do certificado para se alistar, mesmo que já tenha passado os 18 anos.\n\n')


print('1-Sim 2-Não')


while True :
    aceite = int(input('Você concorda com as normas?'))

    if aceite == 1:
        print('Vamos Continuar o Processo...')

        sleep(2)

        hoje = date.today()
        ano = int(input('Digite seu ano de nascimento: '))
        calculo = (hoje.year - ano)
        falta = 18 - calculo
        vencido = calculo - 18

        if calculo == 18:
            print('-' * 20)
            print('Já é hora de se alistar')
        elif calculo < 18:
            print('-' * 20)
            print('Você ainda não tem idade o suficiente para o alistamento\nfaltam {} anos '
                  'para que você possa se alistar,mas fique de olho nas datas.\nAté a proxima!'.format(falta))
        else:
            print('-' * 20)
            print('Ixi, infelizmente você não conseguirá se alistar\njá se passaram {}'
                  ' anos do prazo para seu alistamento.'.format(vencido))
            print('-' * 20)

    elif aceite == 2:
        print ('Obrigada! Tenha um Bom-Dia , processo cancelado.')
        break
    else:
        print ('Opção digitada invalida\nDigite novamente')



