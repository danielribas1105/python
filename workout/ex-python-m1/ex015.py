import math


c1=float(input('Qual o valor do cateto oposto? '))
c2=float(input('Qual o valor do cateto adjacente? '))
print('A hipotenusa deste triângulo vale = {:.2f}'.format(math.sqrt(pow(c1,2)+pow(c2,2))))
