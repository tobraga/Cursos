#Exercício Python 18: Faça um programa que leia um ângulo qualquer 
#e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math 

angulo = float(input('Angulo desejado: '))

seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo, seno))

cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o tangente de {:.2f}'.format(angulo, tangente))

