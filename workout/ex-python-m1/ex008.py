v=float(input("Informe quanto dinheiro tem na carteira = "))
print('Cotação dólar: US$ 1,00 = R$ 3,27')
print('Você poderá comprar US$ {} dólares e sobrará R$ {:.2} reais!'.format(v//3.27,v%3.27))
