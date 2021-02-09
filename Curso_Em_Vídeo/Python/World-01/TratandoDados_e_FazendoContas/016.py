#Exercício Python 15: Escreva um programa que pergunte a 
#quantidade de Km percorridos por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. Calcule
#o preço a pagar, sabendo que o carro custa R$60 por dia 
#e R$0,15 por Km rodado.

km = float(input('Informe a quantidade de Km percorrido: '))
dia = float(input('Informe a quantidade de dias alugado: '))

carroDia = 60 * dia
carroKm = 0.15 * km

print('Total a pagar R$ {:.2f}'.format(carroDia + carroKm))

print('-'*20)