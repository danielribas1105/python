num=int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
base=int(input('Digite uma das opções acima: '))
if base==1:
    print('cálculo binário')
elif base==2:
    print('Cálculo Octal')
else:
    print('Cálculo hexadecimal')