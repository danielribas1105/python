import adivinhacao
import forca

print('*'*16)
print('** GAMES MENU **')
print('*'*16)

print('Selecione o jogo:')
print('(1) - Adivinhação')
print('(2) - Forca')

test=True

while(test):
    select=int(input('Digite um número: '))
    if(1<=select<=2):
        test=False
    else:
        print('JOGO NÂO ENCONTRADO!')

if(select==1):
    adivinhacao.jogar()
if(select==2):
    forca.jogar()