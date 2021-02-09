# Exercício Python 6: Faça um programa que leia um número Inteiro 
# e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Entre com um numero inteiro: '))

print('-' * 20)

print('Antecessor: {}'.format(num - 1))
print('Sucessor: {}'.format(num + 1))