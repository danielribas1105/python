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
    
    print('Selecione o grupo de palavras:')
    print('1 - Frutas')
    print('2 - Carros')
    print('3 - Nomes')
    num=int(input('Digite o número desejado: '))

    if(num == 1):
        grupo='frutas'
    elif(num ==2):
        grupo='carros'
    else:
        grupo='nomes'

    caminho='c:/Users/danie/Documents/GitHub/python/workout/games/'

    with open(caminho+grupo+'.txt', 'r', encoding='UTF-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append (linha)

    palavra_secreta = choice(palavras)

    print('Selecionando a palavra!')
    print('PROCESSANDO...')
    sleep(1)
    print('Grupo de palavras: {} >> A palavra possui {} letras!'.format(grupo.upper(), len(palavra_secreta)))
    sleep(1)

    palavra_forca=['_']*len(palavra_secreta)

    print('Adivinhe a palavra se for capaz!')
    print('Você terá 7 tentativas!')
    sleep(1)
    
    print('Palavra com {} letras'.format(len(palavra_secreta)))
    print(palavra_forca)

    while(not enforcou and not acertou):
        print('Tentativa {} de 7:'.format(tentativa+1))
        chute = input('Digite uma letra ou a palavra: ').lower().strip()
        
        if(chute == palavra_secreta):
            print('PARABÉNS!!! VOCÊ GANHOU!!!')
            print('Você acertou a palavra secreta que era {}.'.format(palavra_secreta.upper()))
            imprime_mensagem_vencedor()
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
                desenha_forca(tentativa)

        if(tentativa==7):
            print('SUAS TENTATIVAS ACABARAM!!!')
            sleep(1)
            print('A palavra sercreta era {}'.format(palavra_secreta.upper()))
            sleep(1)
            print('VOCÊ PERDEU!!!')
            imprime_mensagem_perdedor()
            break

        if(not('_' in palavra_forca)):
            print('PARABÉNS!!! VOCÊ GANHOU!!!')
            print('Você acertou a palavra secreta que era {}.'.format(palavra_secreta.upper()))
            imprime_mensagem_vencedor()
            break
    print("FIM DO JOGO")

#
### FUNÇÕES
#

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_vencedor():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor():
    print("     _______________         ")
    print("    /               \       ")
    print("   /                 \      ")
    print("/\/                   \/\  ")
    print("\ |   XXXX     XXXX   | /   ")
    print(" \|   XXXX     XXXX   |/     ")
    print("  |   XXX       XXX   |      ")
    print("  |                   |      ")
    print("  \__      XXX      __/     ")
    print("    |\     XXX     /|       ")
    print("    | |           | |        ")
    print("    | I I I I I I I |        ")
    print("    |  I I I I I I  |        ")
    print("    \_             _/       ")
    print("      \_         _/         ")
    print("        \_______/           ")


if(__name__ == '__main__'):
    jogar()