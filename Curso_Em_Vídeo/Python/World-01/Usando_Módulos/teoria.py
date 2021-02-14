import math
#form math import sqrt, floor

n = int(input('Entre com um numero: '))

raiz = math.sqrt(n)

print('Raiz do numero {} = {}'.format(n, raiz))
print('Raiz do numero {} arredondado para cima = {}'.format(n, math.ceil(raiz)))
print('Raiz do numero {} arredondado para cima = {}'.format(n, math.floor(raiz)))
print('*' *20)
print('\n')
import random

n2 = random.random() #numero aleatorio entre 0 e 1
n3 = random.randint(1,10) #numero aleatorio entre 1 e 10

print(n2)
print('*' *20)
print('\n')
print(n3) 
print('*' *20)
print('\n')




