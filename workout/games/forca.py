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

    print('Adivinhe a palavra se for capaz!')
    sleep(1)
    print('Palavra com {} letras'.format(len(palavra_secreta)))

    while(not enforcou and not acertou):
        chute = input('Digite uma letra: ').lower().strip()
        
        for letra in palavra_secreta:
            if (chute==letra):
                cont_letra += 1
                print(letra)
                print(palavra_secreta.find(chute))
            i += 1
            enforcou=True
        print('A palavra secreta possui {} letra(s) {}'.format(cont_letra,chute))


if(__name__ == '__main__'):
    jogar()