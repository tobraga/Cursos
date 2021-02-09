#Exercício Python 13: Faça um algoritmo que leia o preço de 
# um produto e mostre seu novo preço, com 5% de desconto


preco = float(input('Entre com o preço do produto [R$]: '))


print('-'*20)

print('Seu novo preço: {:.2f}'.format(preco - (preco * 0.05)))

print('-'*20)
