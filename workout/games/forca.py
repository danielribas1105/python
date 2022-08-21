from time import sleep

def jogar():
    print('*'*19)
    print('** JOGO DA FORCA **')
    print('*'*19)

    palavra_secreta='banana'
    enforcou=False
    acertou=False
    i=0
    cont_letra=0
    erro=1
    palavra_forca=['_']*len(palavra_secreta)
    
    print('Adivinhe a palavra se for capaz!')
    print('Você terá seis tentativas!')
    sleep(1)
    
    print('Palavra com {} letras'.format(len(palavra_secreta)))
    print(palavra_forca)

    while(not enforcou and not acertou):
        print('Tentativa {} de 6:'.format(erro))
        chute = input('Digite uma letra: ').lower().strip()
        
        for letra in palavra_secreta:
            if (chute==letra):
                cont_letra += 1
                palavra_forca[i]=chute
            else:
                erro += 1
            i += 1
        print('A palavra secreta possui {} letra(s) {}'.format(cont_letra,chute))
        print(palavra_forca)
        i=0
        if(not('_' in palavra_forca)):
            print('PARABÉNS!!! VOCÊ GANHOU!!! Acertou a palavra secreta!!!')
            break
        if(erro==6):
            print('SUAS TENTATIVAS ACABARAM!!! VOCÊ PERDEU!!!')
            break
    print("FIM DO JOGO")

if(__name__ == '__main__'):
    jogar()