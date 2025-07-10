import random

print ('🪨 STEIN 🪨 , 🧻 PAPIER 🧻, ✂ SCHERE ✂')

escolha = str(input('Pedra , papel ou tesoura? '))

x = random.choice(['tesoura','pedra','papel'])
y = random.choice(['pedra','papel','tesoura'])

print('Voce escolheu', escolha)
print('O computador escolheu', x)
print('O computador escolheu', y)

if escolha == x:
    print('Empate!')
elif (
    (escolha == 'pedra' and x == 'tesoura') or
    (escolha == 'papel' and x == 'pedra') or
    (escolha == 'tesoura' and x == 'papel'),
    (escolha == 'pedra' and y == 'tesoura') or
    (escolha == 'papel' and y == 'pedra') or
    (escolha == 'tesoura' and y == 'papel')
):
    print('Você venceu!')
else:
    print('Computador venceu!')