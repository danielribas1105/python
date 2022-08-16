from random import randint, random


from random import randint
from time import sleep
n1=int(randint(0,5))
print('Adivinhe o número!!!')
n2=int(input('Digite um número entre 0 e 5:'))
print('PROCESSANDO...')
sleep(3)
if(n1==n2):
    print('Número computador: {} >> Seu número {}'.format(n1,n2))
    print('VOCÊ ACERTOU!!!')
else:
    print('Número computador: {} >> Seu número {}'.format(n1,n2))
    print('VOCÊ ERROU!!!')
print('Fim do Jogo!!!')
