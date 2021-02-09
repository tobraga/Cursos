#Exercício Python 12: Faça um programa que leia a largura e a altura 
# de uma parede em metros, calcule a sua área e a quantidade de tinta 
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma 
# área de 2 metros quadrados.

alt = float(input('Entre com a altura da parede [m]: '))
larg = float(input('Entre com a largura da parede [m]: '))

print('-'*20)
area = alt * larg

print('Area da parede: {:.3f} m²'.format(area))
print('-'*20)
print('A quantidade de tinta para pintar a parede: {:.4f} litros\n'.format(area / 2))