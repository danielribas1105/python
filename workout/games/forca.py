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
    palavra_forca=['_']*len(palavra_secreta)
    
    print('Adivinhe a palavra se for capaz!')
    sleep(1)
    
    print('Palavra com {} letras'.format(len(palavra_secreta)))
    print(palavra_forca)

    while(not enforcou and not acertou):
        chute = input('Digite uma letra: ').lower().strip()
        
        for letra in palavra_secreta:
            if (chute==letra):
                cont_letra += 1
                palavra_forca[i]=chute
            i += 1
        print('A palavra secreta possui {} letra(s) {}'.format(cont_letra,chute))
        print(palavra_forca)
        i=0
        if(not('_' in palavra_forca)):
            break
    print("FIM DO JOGO")

if(__name__ == '__main__'):
    jogar()