#Exercício Python 11: Crie um programa que leia quanto dinheiro
#uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Entre com um valor em reiais que possui R$ '))

print('-'*20)

print('O valor R$ {}, é igual a US$ {:.2f}\n'.format(real, real / 3.27))

print('-'*20)