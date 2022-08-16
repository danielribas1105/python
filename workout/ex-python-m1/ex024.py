f=str(input('Digite uma frase: ')).strip().lower()
print('A frase tem {} letras a'.format(f.count('a')))
print('A letra a aparece pela 1ª vez na posição {}'.format(f.find('a')))
print('A letra a aparece na última posição {}'.format(f.rfind('a')))
