v=float(input('Velocidade do veículo: '))
if v>80:
    print('ACIMA DO LIMITE DE VELOCIDADE >> {} Km/h'.format(v))
    print('MULTA NO VALOR DE {}'.format((v-80)*7))
print('PARABÉNS! VOCÊ ESTÁ ABAIXO DO LIMITE DE 80km/h >> {}'.format(v))
