km=float(input('Quantos Km foram percorridos? '))
d=int(input('Quantos dias de aluguel?'))
print('Total cobrado pelo aluguel = {:.2f}'.format(d*60))
print('Total cobrado pelos Km rodados = {:.2f}'.format(km*0.15))
print('Total a pagar = {:.2f}'.format(d*60+km*0.15))