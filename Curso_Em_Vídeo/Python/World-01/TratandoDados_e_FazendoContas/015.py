#Exercício Python 15: Escreva um programa que converta uma 
# temperatura digitando em graus Celsius e converta para
#  graus Fahrenheit.


cel = float(input('Informe a temperatura em Celsius [C°]: '))


print('-'*20)
fah = 9 * cel / 5 + 32 
print('Temperatura em Fahrenheit [F°]: {:.2f}'.format(fah))

print('-'*20)