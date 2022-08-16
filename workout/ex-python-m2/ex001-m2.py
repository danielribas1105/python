print('\033[35m*'*33)
print('>> CÁLCULO PARA A CASA PRÓPRIA <<')
print('*'*33)
print('\033[m '*33)
casa=float(input('Qual o valor do imóvel? '))
renda=float(input('Qual o valor da renda mensal comprovada? '))
tempo=int(input('Em quantos meses deseja pagar? '))
print('Em {} meses, o valor da prestação seria de R$ {:.2f}'.format(tempo,casa/tempo))
if casa/tempo > renda*0.3:
    print('RECUSADO >> Valor do imóvel ultrapassa as condições do empréstimo.')
else:
    print('APROVADO >> Valor do imóvel de acordo com as condições do empréstimo.')
