s=float(input('Informe o salário: '))
if s>1250:
    print('Aumento de 10% >> Seu novo salário: R$ {:.2f}'.format(s*0.1+s))
else:
    print('Aumento de 15% >> Seu novo salário: R$ {:.2f}'.format(s*0.15+s))
