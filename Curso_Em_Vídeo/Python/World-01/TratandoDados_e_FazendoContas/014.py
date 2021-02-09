#Exercício Python 14: Faça um algoritmo que leia o salário de um 
# funcionário e mostre seu novo salário, com 15% de aumento.


salario = float(input('Entre com o seu salario [R$]: '))


print('-'*20)

print('Seu novo salario: {:.2f}'.format(salario + (salario * 0.15)))

print('-'*20)