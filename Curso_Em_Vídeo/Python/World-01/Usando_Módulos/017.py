#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção Inteira.
import math

num = float(input('Entre com um numero real: '))

inteiro = math.trunc(num)

print ('Parte inteira do numero real: {}'.format(inteiro))
