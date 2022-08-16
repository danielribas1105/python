print('\033[1;31m=' *21)
print('Análise de triângulos')
print('=' *21 + '\033[0m')
num1=float(input('Digite o valor do primeiro lado: '))
num2=float(input('Digite o valor do segundo lado: '))
num3=float(input('Digite o valor do terceiro lado: '))
maior=num1
l2=num2
l3=num3
#if num1<num2+num3 and num2<num1+num3 and num3<num1+num2
if num2>num1 and num2>num3:
    maior=num2
    l2=num1
if num3>num1 and num3>num2:
    maior=num3
    l3=num1
if maior>(abs(l2-l3)) and maior<(l2+l3):
    print('As medidas informadas {}, {} e {}, podem formar um triângulo.'.format(maior,l2,l3))
else:
    print('As medidas informadas {}, {} e {}, não formam um triângulo.'.format(maior,l2,l3))
