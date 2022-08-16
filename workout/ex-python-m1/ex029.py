d=float(input('Qual a distância da viagem?'))
if d<=200:
    p=d*0.5
else:
    p=d*0.45
print('O valor da passagem é de R$ {:.2f}'.format(p))
