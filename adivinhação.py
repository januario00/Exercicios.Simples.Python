import random


print('** ADIVINHE O NUMERO **')

print   ("  ###   "      "  ###   ")
print   (" #   #  "     " #   #  ")
print   ("     #  "     "     #  ")
print   ("    #   "     "    #   ")
print   ("   #    "     "   #    ")
print   ("        "     "        ")
print   ("   #    "     "   #    ")

numero = random.randint (100, 150);

print ('é um numero entre 11 e 13, você tem 5 chances')

for i in range (5):
    acerto = int(input('Qual é o numero?'))
    if acerto == numero:
        print ('🎉VOCE ACERTOU🎉 ')
    elif acerto > numero:
        print('<')
    elif acerto < numero:
        print ('>')
else:
    print('Suas 5 chances acabaram. O número era', numero)
