#Exercício Python 009: Escreva um programa que leia um valor em metros e 
# o exiba convertido em centímetros e milímetros.


metros = float(input('Entre com um valor em Metros[m]: '))


print('-'*20)

print('Metros >>> Centímetros[cm]: {}\n'.format(metros * 100))
print('Metros >>> Milimetros[mm]: {}\n'.format(metros * 1000))