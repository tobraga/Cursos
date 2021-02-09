#Exercício Python 007: Crie um algoritmo que leia um número e 
# mostre o seu dobro, triplo e raiz quadrada.

print('\n')
num = float(input('Entre com um numero: '))

print('-' * 20)

print('Dobro: {}'.format(num * 2))
print('Triplo: {}'.format(num * 3))
print('Raiz Quadrada: {}'.format(num ** 0.5)) # pow(num, (1/2)) pow(num, 0.5)
