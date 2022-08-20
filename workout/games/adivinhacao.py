from random import randint
from time import sleep

def jogar():
    print('*'*25)
    print('** JOGO DA ADIVINHAÇÃO **')
    print('*'*25)

    n1=int(randint(0,10))
    rodada=0
    tentar=True

    print('Estou pensando em um número de 0 a 10. Você consegue acertar? Serão três tentativas.')
    sleep(2)
    print('Vamos jogar!')
    sleep(2)

    while(rodada<3 and tentar):
        print('Rodada {} de 3'.format(rodada+1))
        n2=int(input('Digite um número entre 0 e 10: '))
        while(n2<0 or n2>10):
            print("Você digitou o número {}. Número inválido!!!".format(n2))
            n2=int(input('Digite um número entre 0 e 10: '))
        print('PROCESSANDO...')
        sleep(2)
        if(n1==n2):
            print('Número pensado: {} >> Seu número {}'.format(n1,n2))
            print('PARABÉNS!!! VOCÊ ACERTOU!!!')
            tentar=False
        elif(n1<n2):
            print('Você digitou um número maior!')
        else:   
            print('Você digitou um número menor!') 
        rodada += 1

    if(tentar):
        print('VOCÊ NÃO ADIVINHOU!!!GAME OVER!!!')
    print("FIM DO JOGO!!!")


if(__name__ == '__main__'):
    jogar()