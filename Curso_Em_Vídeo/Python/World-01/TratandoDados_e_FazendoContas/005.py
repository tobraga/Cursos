
n = input('Entre com algo do teclado: ')

print(type(n))
print('É numerico: {}'.format(n.isnumeric()))
print('É alfabético: {}'.format(n.isalpha()))
print('É alfanumerico: {}'.format(n.isalnum()))
print('Está em lestras maiusculas: {}'.format(n.isupper()))