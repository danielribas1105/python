from time import sleep
from random import choice

def jogar():
    print('*'*19)
    print('** JOGO DA FORCA **')
    print('*'*19)

    enforcou=False
    acertou=False
    palavras=[]
    cont_letra=0
    tentativa=0
    
    with open('c:/Users/danie/Documents/GitHub/python/workout/games/frutas.txt', 'r', encoding='UTF-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append (linha)
    
    #arquivo = open('c:/Users/danie/Documents/GitHub/python/workout/games/frutas.txt', 'r')
    #for linha in arquivo:
    #    linha = linha.strip()
    #    palavras.append (linha)
    #arquivo.close()

    #print(palavras[0])
    #print(len(palavras[0]))

    palavra_secreta = choice(palavras)

    print('Selecionando a palavra!')
    print('PROCESSANDO...')
    sleep(1)
    print('A palavra é uma fruta e possui {} letras!'.format(len(palavra_secreta)))
    sleep(1)

    palavra_forca=['_']*len(palavra_secreta)

    print('Adivinhe a palavra se for capaz!')
    print('Você terá seis tentativas!')
    sleep(1)
    
    print('Palavra com {} letras'.format(len(palavra_secreta)))
    print(palavra_forca)

    while(not enforcou and not acertou):
        print('Tentativa {} de 6:'.format(tentativa+1))
        chute = input('Digite uma letra ou a palavra: ').lower().strip()
        
        if(chute == palavra_secreta):
            print('PARABÉNS!!! VOCÊ GANHOU!!!')
            print('Você acertou a palavra secreta que era {}.'.format(palavra_secreta.upper()))
            break
        else:
            if(chute in palavra_secreta):
                tentativa += 1
                i=0
                for letra in palavra_secreta:
                    if (chute==letra):
                        cont_letra += 1
                        palavra_forca[i]=chute 
                    i += 1
                print('A palavra secreta possui {} letra(s) {}'.format(cont_letra,chute))
                print(palavra_forca)
                i=0
                cont_letra=0
            else:
                print('Letra {} não encontrada na palavra! Tente novamente!'.format(chute))
                tentativa += 1

        if(tentativa==6):
            print('SUAS TENTATIVAS ACABARAM!!!')
            sleep(1)
            print('A palavra sercreta era {}'.format(palavra_secreta.upper()))
            sleep(1)
            print('VOCÊ PERDEU!!!')
            break

        if(not('_' in palavra_forca)):
            print('PARABÉNS!!! VOCÊ GANHOU!!!')
            print('Você acertou a palavra secreta que era {}.'.format(palavra_secreta.upper()))
            break
    print("FIM DO JOGO")

if(__name__ == '__main__'):
    jogar()